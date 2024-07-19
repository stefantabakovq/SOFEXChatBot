from dependency_injector import containers, providers
from src.Configs.SofexAIConfig import SofexAIConfig


class SofexAIContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    # API CONFIGURATIONS
    ai_config = providers.Singleton(
        SofexAIConfig,
        model_name=config.SofexAI.model_name,
        max_tokens=config.SofexAI.max_tokens
    )
