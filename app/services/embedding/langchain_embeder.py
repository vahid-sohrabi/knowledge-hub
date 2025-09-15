from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from .base_embeder import AbstractEmbedding
from app.config.settings import settings


class LangChainEmbeder(AbstractEmbedding):
    """
    Embedding implementation using LangChain embeddings.
    Always uses the model defined in Settings.
    """

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=settings.embedding_model_name)

    def embed_text(self, text: str) -> List[float]:
        """
        Convert a single text string into a vector embedding.
        """
        result = self.embedding_model.embed_documents([text])
        return result[0]

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Convert a list of text strings into a list of embedding vectors.
        """
        return self.embedding_model.embed_documents(texts)
