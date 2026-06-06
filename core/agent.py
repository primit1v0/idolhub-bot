from pocketflow import Node, Flow
from core.config import AppConfig
from core.llm import call_llm
from memory.sqlite_store import SqliteStore
from core.llm import call_llm

class AnswerNode(Node):
    def __init__(self, cfg: AppConfig):
        super().__init__()
        self.cfg = cfg

    def prep(self, shared: dict):
        return shared.get("messages", [])

    def exec(self, messages: list) -> str:
        response = call_llm(self.cfg, messages)
        return response

    def post(self, shared: dict, prep_res: list, exec_res: str):
        shared["response"] = exec_res


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
        
        shared = {"messages": messages}
        self.flow.run(shared)
        response = shared.get("response", "")
        
        await self.memory.add_message(user_id, "user", user_input)
        await self.memory.add_message(user_id, "assistant", response)
        
        return response
