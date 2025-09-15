from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Vector DB
    qdrant_url: str = Field("http://10.0.84.117:6333", env="QDRANT_URL")
    qdrant_api_key: str = Field("QdrantStrongApiKey123", env="QDRANT_API_KEY")
    collection_name: str = Field("knowledge_docs", env="COLLECTION_NAME")

    # Embedding model
    embedding_model_name: str = Field(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        env="EMBEDDING_MODEL"
    )

    # Text chunking
    chunk_size: int = Field(500, env="CHUNK_SIZE")
    chunk_overlap: int = Field(50, env="CHUNK_OVERLAP")

    # QA model
    qa_model_name: str = Field("deepset/roberta-base-squad2", env="QA_MODEL")

    # Other
    top_k: int = Field(5, env="TOP_K")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
