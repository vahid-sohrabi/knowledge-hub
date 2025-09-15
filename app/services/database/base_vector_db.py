from abc import ABC, abstractmethod
from typing import List, Dict

class AbstractVectorDB(ABC):
    """Interface for vector database operations."""

    @abstractmethod
    def create_collection(self, collection_name: str):
        pass

    @abstractmethod
    def upsert(self, collection_name: str, ids: List[str], vectors: List[List[float]], payloads: List[Dict]):
        pass

    @abstractmethod
    def query(self, collection_name: str, vector: List[float], top_k: int = 5) -> List[Dict]:
        pass
