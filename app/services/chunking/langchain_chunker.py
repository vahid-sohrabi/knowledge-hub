from typing import List
from langchain_text_splitters import CharacterTextSplitter
from .base_chunker import AbstractChunker


class RecursiveChunker(AbstractChunker):
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )

    def chunk(self, text: str) -> List[str]:
        # CharacterTextSplitter returns list of strings
        return self.splitter.split_text(text)
