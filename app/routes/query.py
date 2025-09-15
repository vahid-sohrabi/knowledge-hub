from fastapi import APIRouter
from app.services.qdrant_service import client
from app.services.embedding_service import get_embedding

router = APIRouter()

COLLECTION_NAME = "knowledge_hub"

@router.get("/query/")
def query_rag(question: str):
    q_embedding = get_embedding(question)
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=q_embedding,
        limit=5
    )
    results = [hit.payload.get("text") for hit in hits]
    return {"results": results}
