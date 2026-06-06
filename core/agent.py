import json
import inspect
import re
from pocketflow import AsyncNode, AsyncFlow
from core.config import AppConfig
from core.llm import call_llm
from memory.sqlite_store import SqliteStore
from tools.registry import TOOLS_SCHEMA, TOOLS_MAPPING
from core.event_bus import EventBus
from plugins.loader import load_plugins
from skills.loader import load_skills

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
        self.tools_schema = list(TOOLS_SCHEMA)
        self.tools_mapping = dict(TOOLS_MAPPING)
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
        await self.memory.initialize()
        
        # Load Skills & Plugins
        load_skills(self.cfg.skills.dir, self.cfg, self.tools_schema, self.tools_mapping)
        load_plugins(self.cfg.plugins.dir, self.event_bus)

    async def close(self):
        if hasattr(self, 'memory') and self.memory:
            await self.memory.close()

    async def run(self, user_id: str, user_input: str) -> str:
        """Run the agent asynchronously with the given user input."""
        ctx = {"user_id": user_id, "user_input": user_input}
        await self.event_bus.emit("before_message", ctx)
        
        user_id = ctx.get("user_id", user_id)
        user_input = ctx.get("user_input", user_input)
        
        history = await self.memory.get_history(user_id)
        
        messages = []
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_input})
        
        # Retrieve facts and filter them locally
        facts = await self.memory.get_fakta(user_id, limit=30)
        query_words = set(re.findall(r'[a-zA-Z0-9]+', user_input.lower()))
        relevant_facts = []
        for fact in facts:
            entity = fact.get("entity", "")
            entity_words = set(re.findall(r'[a-zA-Z0-9]+', entity.lower()))
            if query_words.intersection(entity_words):
                relevant_facts.append(fact)
        
        relevant_facts = relevant_facts[:3]
        if relevant_facts:
            facts_md = "Relevant facts:\n" + "\n".join(f"- {f['entity']}: {f['nilai']}" for f in relevant_facts)
            messages.insert(0, {"role": "system", "content": facts_md})
        
        await self.memory.add_message(user_id, "user", user_input)
        
        await self.event_bus.emit("after_message", ctx)
        
        shared = {
            "messages": messages,
            "tools_schema": self.tools_schema,
            "user_id": user_id,
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
        
        await self.memory.add_message(user_id, "assistant", final_text)
        
        await self.event_bus.emit("after_reply", ctx)
        return final_text
