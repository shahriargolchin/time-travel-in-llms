from services.base_client import BaseClient
from transformers import pipeline


class TransformersClient(BaseClient):
    def __init__(
        self, generation_kwargs=None, huggingface_pipeline_kwargs=None
    ) -> None:
        super().__init__()
        self.client = None
        self.generation_kwargs = generation_kwargs or {}
        self.huggingface_pipeline_kwargs = huggingface_pipeline_kwargs or {}

    def get_text(
        self,
        text,
        model,
        max_tokens=500,
        temperature=0,
        top_p=1,
        frequency_penalty=1.0,  # not used here
        presence_penalty=1.0,  # default in HF is 1.0 not 0.0
    ):
        if self.client is None:
            self.client = pipeline(
                model=model, task="text-generation", **self.huggingface_pipeline_kwargs
            )

        map_generation_kwargs = {
            "max_new_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "repetition_penalty": presence_penalty,
        }

        # TODO update the generation and hugginface pipeline args according to def and map openAI style
        try:
            response = self.client(text, **map_generation_kwargs)
        except Exception as e:
            raise Exception(
                f"Failed to generate text with Transformers pipeline: {str(e)}"
            )

        if response:
            return response[0]["generated_text"]
        else:
            raise Exception("Response from Transformers pipeline is empty.")
