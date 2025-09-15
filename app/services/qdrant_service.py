from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

from app.config import settings

client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)

def create_collection(collection_name: str):
    try:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )
    except Exception:
        pass

def upsert_vectors(collection_name: str, vectors: list):
    client.upsert(collection_name=collection_name, points=vectors)
