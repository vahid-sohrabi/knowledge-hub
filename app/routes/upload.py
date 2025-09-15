from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
from app.services.embedding_service import get_embedding
from app.services.qdrant_service import upsert_vectors, create_collection

router = APIRouter()

COLLECTION_NAME = "knowledge_hub"


@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    embedding = get_embedding(text)

    create_collection(COLLECTION_NAME)
    upsert_vectors(COLLECTION_NAME, [{"id": file.filename, "vector": embedding, "payload": {"text": text}}])

    return {"message": "PDF uploaded and processed successfully."}
