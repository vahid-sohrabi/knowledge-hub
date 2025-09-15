from abc import ABC, abstractmethod
from typing import List


class AbstractChunker(ABC):
    """Interface for text chunking strategies."""

    @abstractmethod
    def chunk(self, text: str) -> List[str]:
        pass
