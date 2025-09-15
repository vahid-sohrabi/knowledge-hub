from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    llama_model_path: str = "path/to/llama-model"
    openai_api_key: str = "YOUR_OPENAI_API_KEY"

settings = Settings()
