from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_text(
        self,
        text,
        model,
        max_tokens=500,
        temperature=0.0,
        top_p=1.00,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    ):
        raise NotImplementedError()

    def from_libary(
        api_client: str, generation_kwargs=None, huggingface_pipeline_kwargs=None
    ):
        if api_client == "openai":
            from services.openai_api import OpenAIClient

            return OpenAIClient()
        elif api_client == "huggingface":
            from services.transformer_api import TransformersClient

            return TransformersClient(
                generation_kwargs=generation_kwargs,
                huggingface_pipeline_kwargs=huggingface_pipeline_kwargs,
            )
