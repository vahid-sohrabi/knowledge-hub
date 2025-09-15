from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from typing import List, Dict
from .base_vector_db import AbstractVectorDB
from app.config.settings import settings


class QdrantDB(AbstractVectorDB):
    """Qdrant implementation of vector database using settings."""

    def __init__(self, url: str = None):
        self.url = url or settings.qdrant_url
        self.client = QdrantClient(url=self.url)

    def create_collection(self, collection_name: str = None, vector_size: int = 384, distance: str = "Cosine"):
        """
        Create or recreate a collection in Qdrant.
        - collection_name: optional, uses Settings.collection_name if None
        - vector_size: size of embedding vectors
        - distance: similarity metric
        """
        collection_name = collection_name or settings.collection_name
        existing = [c.name for c in self.client.get_collections().collections]
        if collection_name not in existing:
            self.client.recreate_collection(
                collection_name=collection_name,
                vectors_config={"size": vector_size, "distance": distance}
            )

    def upsert(self, collection_name: str, ids: List[str], vectors: List[List[float]], payloads: List[Dict]):
        """
        Upsert points into Qdrant collection.
        """
        points = [PointStruct(id=id_, vector=vec, payload=pl) for id_, vec, pl in zip(ids, vectors, payloads)]
        self.client.upsert(collection_name=collection_name, points=points)

    def query(self, collection_name: str, vector: List[float], top_k: int = None) -> List[Dict]:
        """
        Query top-k similar vectors from Qdrant.
        """
        top_k = top_k or settings.top_k
        response = self.client.search(collection_name=collection_name, query_vector=vector, limit=top_k)
        return [{"id": p.id, "score": p.score, "payload": p.payload} for p in response]
