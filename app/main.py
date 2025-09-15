from fastapi import FastAPI
from app.routes import upload, query


app = FastAPI(title="Knowledge Hub RAG API")

app.include_router(upload.router, prefix="/pdf")
app.include_router(query.router, prefix="/rag")