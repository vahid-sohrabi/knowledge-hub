from abc import ABC, abstractmethod
from typing import List


class AbstractLoader(ABC):
    """Base interface for all document loaders."""

    @abstractmethod
    def load_documents(self) -> List[dict]:
        """
        Load the file and return a list of document dicts.
        Each dict can have keys like 'text', 'metadata', etc.
        """
        pass

    @abstractmethod
    def load_texts(self) -> List[str]:
        """Extract text content as a list of strings."""
        pass
