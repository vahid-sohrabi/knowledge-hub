# app/services/pipeline/rag_pipeline.py
from typing import List
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline as hf_pipeline
from app.services.loader.universal_loader import UniversalLoader
from app.services.chunking.langchain_chunker import RecursiveChunker
from app.services.embedding.langchain_embeder import LangChainEmbeder
from app.services.database.qdrant_db import QdrantDB
from app.config.settings import settings


class RAGPipeline:
    """
    Complete Retrieval-Augmented Generation (RAG) pipeline:
    1. Ingest files (chunk, embed, store)
    2. Retrieve relevant chunks from Qdrant
    3. Generate answer with QA model
    """

    def __init__(self):
        # Components
        self.loader_cls = UniversalLoader
        self.chunker = RecursiveChunker(
            chunk_size=settings.chunk_size,
            overlap=settings.chunk_overlap
        )
        self.embedder = LangChainEmbeder()
        self.vector_db = QdrantDB()

        # Load QA model and tokenizer from settings
        self.qa_tokenizer = AutoTokenizer.from_pretrained(settings.qa_model_name)
        self.qa_model = AutoModelForQuestionAnswering.from_pretrained(settings.qa_model_name)
        self.qa_pipeline = hf_pipeline(
            task="question-answering",
            model=self.qa_model,
            tokenizer=self.qa_tokenizer
        )

    # Indexing / Ingestion
    def ingest_file(self, file_path: str, doc_id: str):
        loader = self.loader_cls(file_path)
        texts = loader.load_texts()
        for i, text in enumerate(texts):
            # Chunking
            chunks: List[str] = self.chunker.chunk(text)
            # Embedding
            embeddings: List[List[float]] = self.embedder.embed_texts(chunks)
            # Prepare payloads
            vector_ids = [f"{doc_id}_chunk_{i}_{j}" for j in range(len(chunks))]
            vector_payloads = [{"text": chunk} for chunk in chunks]

            # Save to Qdrant
            self.vector_db.create_collection()
            self.vector_db.upsert(
                collection_name=settings.collection_name,
                ids=vector_ids,
                vectors=embeddings,
                payloads=vector_payloads
            )

    # Retrieval
    def retrieve(self, query: str, top_k: int = None) -> List[str]:
        # Embed query
        query_vector = self.embedder.embed_text(query)
        # Retrieve top-k relevant chunks
        results = self.vector_db.query(
            collection_name=settings.collection_name,
            vector=query_vector,
            top_k=top_k
        )
        return [r["payload"]["text"] for r in results]

    # Question Answering
    def answer(self, query: str, top_k: int = None) -> str:
        relevant_texts = self.retrieve(query, top_k)
        context = " ".join(relevant_texts)
        result = self.qa_pipeline(question=query, context=context)
        return result.get("answer", "")
