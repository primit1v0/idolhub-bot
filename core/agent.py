from pocketflow import Node, Flow
from core.config import AppConfig
from core.llm import call_llm

class AnswerNode(Node):
    def __init__(self, cfg: AppConfig):
        super().__init__()
        self.cfg = cfg

    def prep(self, shared: dict):
        return shared.get("user_input", "")

    def exec(self, user_input: str) -> str:
        messages = [{"role": "user", "content": user_input}]
        response = call_llm(self.cfg, messages)
        return response

    def post(self, shared: dict, prep_res: str, exec_res: str):
        shared["response"] = exec_res


class IdolhubAgent:
    def __init__(self, cfg: AppConfig):
        self.cfg = cfg
        self._build_flow()

    def _build_flow(self):
        """Build the PocketFlow execution graph."""
        # Saat ini flow masih sangat sederhana: Input -> AnswerNode
        # Ke depan akan kita inject DecideAction, UseTool, dan Memory
        
        self.answer_node = AnswerNode(self.cfg)
        self.flow = Flow(start=self.answer_node)

    def run(self, user_input: str) -> str:
        """Run the agent with the given user input."""
        shared = {"user_input": user_input}
        self.flow.run(shared)
        return shared.get("response", "")
