from dependency_injector.wiring import Provide, inject

from src.Configs.SofexAIConfig import SofexAIConfig
from src.Containers.SofexAIContainer import SofexAIContainer
from src.Models.AI import AI

from gpt4all import GPT4All


class SofexAI(AI):
    @inject
    def __init__(self, config: SofexAIConfig = Provide[SofexAIContainer.ai_config]):
        super().__init__()
        self.Model = None
        self.model_name = config.model_name
        self.max_tokens = config.max_tokens

    def create_model(self):
        model = GPT4All(self.model_name)
        self.Model = model
        return model

    def generate_answer(self) -> str:
        with self.Model.chat_session():
            return self.Model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=self.max_tokens)
