from abc import ABC, abstractmethod
from typing import List


class AbstractEmbedding(ABC):
    """Base class for all embedding strategies."""

    @abstractmethod
    def embed_text(self, text: str) -> List[float]:
        """Convert a single text string into a vector embedding."""
        pass

    @abstractmethod
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Convert a list of text strings into a list of embedding vectors."""
        pass
