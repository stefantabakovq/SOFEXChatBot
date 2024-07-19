from src.Models.Config import Config


class SofexAIConfig(Config):
    def __init__(self, model_name, max_tokens):
        super().__init__()
        self.model_name = model_name
        self.max_tokens = max_tokens
