# app/main.py
from fastapi import FastAPI
from app.api.file_upload_api import FileUploadAPI
from app.api.question_api import QuestionAPI
from app.exception.api_exception import ApiException
from app.exception.handler.general_error_handler import GeneralErrorHandler
from app.services.pipeline.rag_pipeline import RAGPipeline
from app.services.loader.registry.file_registry import FileTypeRegistry
from app.services.loader.registry.file_type import FileType
from app.services.loader.excel_loader import ExcelLoader
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
import uvicorn

# --- Create FastAPI app ---
app = FastAPI(title="Knowledge Hub RAG API")

# --- Register default loaders for common file types ---
FileTypeRegistry.register(FileType.PDF, lambda path: PyPDFLoader(path))
FileTypeRegistry.register(FileType.TXT, lambda path: TextLoader(path))
FileTypeRegistry.register(FileType.DOC, lambda path: UnstructuredWordDocumentLoader(path))
FileTypeRegistry.register(FileType.DOCX, lambda path: UnstructuredWordDocumentLoader(path))
FileTypeRegistry.register(FileType.XLS, lambda path: ExcelLoader(path))
FileTypeRegistry.register(FileType.XLSX, lambda path: ExcelLoader(path))

# --- Initialize RAG pipeline ---
rag_pipeline = RAGPipeline()

# --- Register central error handler ---
error_handler = GeneralErrorHandler()
app.add_exception_handler(ApiException, error_handler.handle_exception)

# --- Initialize API classes and include routers ---
upload_api = FileUploadAPI(pipeline=rag_pipeline)
question_api = QuestionAPI(pipeline=rag_pipeline)

app.include_router(upload_api.router)
app.include_router(question_api.router)

if __name__ == "__main__":
    # Run FastAPI app with uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
