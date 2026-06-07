import inspect
import json
import re

from pocketflow import AsyncFlow, AsyncNode

from core.config import AppConfig
from core.event_bus import EventBus
from core.llm import call_llm
from core.rag_filter import filter_query
from memory.sqlite_store import SqliteStore
from plugins.loader import load_plugins
from skills.loader import load_skills
from tools.registry import TOOLS_MAPPING, TOOLS_SCHEMA


class AnswerNode(AsyncNode):
    def __init__(self, cfg: AppConfig):
        # Retry up to 3 times, with 1 second delay
        super().__init__(max_retries=3, wait=1)
        self.cfg = cfg

    async def prep_async(self, shared: dict):
        return shared

    async def exec_async(self, shared: dict) -> dict:
        messages = shared.get("messages", [])
        tools_schema = shared.get("tools_schema", [])
        
        if shared.get("iters", 0) >= self.cfg.agent.max_iterations:
            return {"type": "error", "content": "Error: Too many iterations."}
            
        result = await call_llm(self.cfg, messages, tools=tools_schema)
        return result

    async def post_async(self, shared: dict, prep_res: dict, exec_res: dict):
        shared["iters"] = shared.get("iters", 0) + 1
        shared["llm_result"] = exec_res
        
        if exec_res.get("type") == "text":
            shared["final_text"] = exec_res["content"]
            return "done"
        elif exec_res.get("type") == "error":
            shared["final_text"] = exec_res["content"]
            return "done"
        elif exec_res.get("type") == "tool_calls":
            return "tool_call"


class ToolExecutionNode(AsyncNode):
    def __init__(self, cfg: AppConfig, tools_mapping: dict, event_bus: EventBus, memory):
        super().__init__()
        self.cfg = cfg
        self.tools_mapping = tools_mapping
        self.event_bus = event_bus
        self.memory = memory

    async def prep_async(self, shared: dict):
        return shared

    async def exec_async(self, shared: dict) -> dict:
        llm_result = shared.get("llm_result", {})
        messages = shared.get("messages", [])
        user_id = shared.get("user_id")
        user_input = shared.get("user_input", "")
        
        messages.append(llm_result["message_obj"])
        
        for tc in llm_result["calls"]:
            func_name = tc.function.name
            try:
                args = json.loads(tc.function.arguments)
            except Exception:
                args = {}
                
            tool_ctx = {
                "user_id": user_id,
                "tool_name": func_name,
                "tool_args": args,
                "agent_context": messages
            }
            await self.event_bus.emit("on_tool_call", tool_ctx)
            
            if func_name in self.tools_mapping:
                func = self.tools_mapping[func_name]
                sig = inspect.signature(func)
                extra_args = {}
                if "user_id" in sig.parameters:
                    extra_args["user_id"] = user_id
                if "memory" in sig.parameters:
                    extra_args["memory"] = self.memory
                if "user_input" in sig.parameters:
                    extra_args["user_input"] = user_input
                if "gating_enabled" in sig.parameters:
                    extra_args["gating_enabled"] = self.cfg.agent.gating_enabled
                
                func_result = func(**{**args, **extra_args})
                if inspect.iscoroutine(func_result):
                    func_result = await func_result
            else:
                func_result = f"Error: Tool {func_name} not found"
                
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "name": func_name,
                "content": str(func_result)
            })
            
        return shared

    async def post_async(self, shared: dict, prep_res: dict, exec_res: dict):
        return "default"


class IdolhubAgent:
    def __init__(self, cfg: AppConfig):
        self.cfg = cfg
        self.event_bus = EventBus()
        
        # Filter tools based on config.json (load all if enabled is empty)
        self.tools_schema = []
        self.tools_mapping = {}
        enabled_tools = self.cfg.tools.enabled
        for schema in TOOLS_SCHEMA:
            name = schema["function"]["name"]
            if not enabled_tools or name in enabled_tools:
                self.tools_schema.append(schema)
                self.tools_mapping[name] = TOOLS_MAPPING[name]
                
        self.memory = SqliteStore(self.cfg)
        self._build_flow()

    def _build_flow(self):
        """Build the PocketFlow execution graph."""
        self.answer_node = AnswerNode(self.cfg)
        self.tool_node = ToolExecutionNode(self.cfg, self.tools_mapping, self.event_bus, self.memory)
        
        # Wire graph using PocketFlow custom transition operators
        self.answer_node - "tool_call" >> self.tool_node
        self.answer_node - "done" >> None
        self.tool_node >> self.answer_node
        
        self.flow = AsyncFlow(start=self.answer_node)

    async def initialize(self):
        # Initialize memory only if enabled
        if self.cfg.agent.memory_enabled:
            await self.memory.initialize()
        
        # Load Skills & Plugins
        load_skills(self.cfg.skills.dir, self.cfg, self.tools_schema, self.tools_mapping)
        load_plugins(self.cfg.plugins.dir, self.event_bus, self.cfg.plugins.enabled)

    async def close(self):
        if hasattr(self, 'memory') and self.memory:
            await self.memory.close()

    async def run(self, user_id: str, user_input: str) -> str:
        """Run the agent asynchronously with the given user input."""
        ctx = {"user_id": user_id, "user_input": user_input}
        await self.event_bus.emit("before_message", ctx)
        
        user_id = ctx.get("user_id", user_id)
        user_input = ctx.get("user_input", user_input)

        # Check prompt injection
        if self.cfg.agent.filter_enabled:
            filtered = filter_query(user_input)
            if filtered["status"] == "BLOCKED":
                return "Maaf, permintaan Anda tidak dapat diproses demi alasan keamanan."
        
        # Get history only if memory is enabled
        history = []
        if self.cfg.agent.memory_enabled:
            history = await self.memory.get_history(user_id)
        
        messages = []
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_input})
        
        # 1. Retrieve & Rank Facts (only if memory enabled)
        scored_facts = []
        if self.cfg.agent.memory_enabled:
            facts = await self.memory.get_fakta(user_id, limit=30)
            query_words = set(re.findall(r'[a-zA-Z0-9]+', user_input.lower()))
            for i, fact in enumerate(facts):
                entity = fact.get("entity", "")
                entity_words = set(re.findall(r'[a-zA-Z0-9]+', entity.lower()))
                intersection = query_words.intersection(entity_words)
                if intersection:
                    sim_score = len(intersection) / len(entity_words) if entity_words else 0.0
                    rec_score = 1.0 - (i / len(facts)) if len(facts) > 1 else 1.0
                    conf_score = fact.get("confidence", 0.9)
                    score = (0.5 * sim_score) + (0.3 * rec_score) + (0.2 * conf_score)
                    scored_facts.append((score, fact))
            scored_facts.sort(key=lambda x: x[0], reverse=True)
        
        # 2. Retrieve FTS5 matching messages (only if memory enabled)
        unique_fts = []
        if self.cfg.agent.memory_enabled:
            fts_messages = await self.memory.search_history_fts(user_id, user_input, limit=3)
            recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else [m["content"] for m in messages]
            unique_fts = [m for m in fts_messages if m.get("matched_content", m["content"]) not in recent_contents]

        # 2b. Retrieve semantic matching messages (only if memory enabled)
        unique_semantic = []
        if self.cfg.agent.memory_enabled and self.cfg.memory.long_term.backend == "sqlite_vec":
            semantic_messages = await self.memory.search_history_semantic(
                user_id, user_input, limit=3
            )
            recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else [m["content"] for m in messages]
            unique_semantic = [
                message
                for message in semantic_messages
                if message["content"] not in recent_contents
            ]

        # 3. Reciprocal Rank Fusion (RRF) Merger
        # We assign rank score = 1 / (60 + rank)
        rrf_map = {}
        for rank, (_, fact) in enumerate(scored_facts):
            item = f"Fakta: {fact['entity']} -> {fact['nilai']}"
            rrf_map[item] = rrf_map.get(item, 0.0) + (1.0 / (60.0 + rank))
        for rank, msg in enumerate(unique_fts):
            item = f"Pesan lampau ({msg['role']}): {msg['content']}"
            rrf_map[item] = rrf_map.get(item, 0.0) + (1.0 / (60.0 + rank))
        for rank, msg in enumerate(unique_semantic):
            item = f"Pesan lampau ({msg['role']}): {msg['content']}"
            rrf_map[item] = rrf_map.get(item, 0.0) + (1.0 / (60.0 + rank))
            
        # Sort combined by RRF score DESC and limit to top 3
        rrf_items = [(score, item) for item, score in rrf_map.items()]
        rrf_items.sort(key=lambda x: x[0], reverse=True)
        top_rrf = [item[1] for item in rrf_items[:3]]
        
        if top_rrf:
            rrf_md = "Relevant context (RRF ranked):\n" + "\n".join(f"- {item}" for item in top_rrf)
            messages.insert(0, {"role": "system", "content": rrf_md})
        
        # Add message to memory only if enabled
        if self.cfg.agent.memory_enabled:
            await self.memory.add_message(user_id, "user", user_input)
        
        await self.event_bus.emit("after_message", ctx)
        
        shared = {
            "messages": messages,
            "tools_schema": self.tools_schema if self.cfg.agent.tools_enabled else [],
            "user_id": user_id,
            "user_input": user_input,
            "iters": 0
        }
        
        try:
            await self.flow.run_async(shared)
        except Exception as e:
            ctx["error"] = e
            await self.event_bus.emit("on_error", ctx)
            raise e
            
        final_text = shared.get("final_text", "Error: Too many iterations.")
        
        ctx["response"] = final_text
        await self.event_bus.emit("before_reply", ctx)
        final_text = ctx.get("response", final_text)
        
        # Add assistant message to memory only if enabled
        if self.cfg.agent.memory_enabled:
            await self.memory.add_message(user_id, "assistant", final_text)
        
        await self.event_bus.emit("after_reply", ctx)
        return final_text
