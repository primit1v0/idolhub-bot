from pocketflow import Node, Flow
from core.config import AppConfig
from core.llm import call_llm
from memory.sqlite_store import SqliteStore
from tools.registry import TOOLS_SCHEMA, TOOLS_MAPPING
import json

class AnswerNode(Node):
    def __init__(self, cfg: AppConfig):
        super().__init__()
        self.cfg = cfg

    def prep(self, shared: dict):
        return shared

    def exec(self, shared: dict) -> dict:
        messages = shared.get("messages", [])
        result = call_llm(self.cfg, messages, tools=TOOLS_SCHEMA)
        return result

    def post(self, shared: dict, prep_res: dict, exec_res: dict):
        shared["llm_result"] = exec_res


class IdolhubAgent:
    def __init__(self, cfg: AppConfig):
        self.cfg = cfg
        self._build_flow()

    def _build_flow(self):
        """Build the PocketFlow execution graph."""
        self.answer_node = AnswerNode(self.cfg)
        self.flow = Flow(start=self.answer_node)

    async def initialize(self):
        self.memory = SqliteStore(self.cfg)
        await self.memory.initialize()

    async def close(self):
        if hasattr(self, 'memory') and self.memory:
            await self.memory.close()

    async def run(self, user_id: str, user_input: str) -> str:
        """Run the agent with the given user input and memory context."""
        history = await self.memory.get_history(user_id)
        
        messages = []
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_input})
        
        # Simpan user msg
        await self.memory.add_message(user_id, "user", user_input)
        
        max_iters = 5
        iters = 0
        final_text = ""
        
        while iters < max_iters:
            shared = {"messages": messages}
            self.flow.run(shared)
            
            result = shared.get("llm_result", {})
            
            if result.get("type") == "text":
                final_text = result["content"]
                break
                
            elif result.get("type") == "tool_calls":
                msg_obj = result["message_obj"]
                messages.append(msg_obj)
                
                # Simpan niat tool call ke memory sebagai referensi
                tool_names = [tc.function.name for tc in result["calls"]]
                await self.memory.add_message(user_id, "assistant", f"[Menggunakan Tool: {', '.join(tool_names)}]")
                
                for tc in result["calls"]:
                    func_name = tc.function.name
                    try:
                        args = json.loads(tc.function.arguments)
                    except:
                        args = {}
                        
                    if func_name in TOOLS_MAPPING:
                        func_result = TOOLS_MAPPING[func_name](**args)
                    else:
                        func_result = f"Error: Tool {func_name} not found"
                        
                    # Simpan hasil tool ke memory
                    await self.memory.add_message(user_id, "tool", str(func_result))
                        
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "name": func_name,
                        "content": str(func_result)
                    })
            iters += 1
            
        if not final_text:
            final_text = "Error: Too many iterations."
            
        await self.memory.add_message(user_id, "assistant", final_text)
        return final_text
