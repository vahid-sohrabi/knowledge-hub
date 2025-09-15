from typing import List
from .base_loader import AbstractLoader
from app.services.loader.registry.file_registry import FileTypeRegistry


class UniversalLoader(AbstractLoader):
    """
    General-purpose loader for multiple file types.
    Uses FileTypeRegistry to select loader.
    Follows Single Responsibility and Open/Closed principles:
    - SRP: Only responsible for loading content.
    - OCP: New file types can be added by registering new loaders in FileTypeRegistry.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        # Get the appropriate loader from FileTypeRegistry
        self.loader = FileTypeRegistry.get_loader(file_path)

    def load_documents(self) -> List[dict]:
        """
        Return a list of document dicts with 'text' key.
        Each dict represents a document.
        """
        return self.loader.load()

    def load_texts(self) -> List[str]:
        """
        Return extracted text content as a list of strings.
        """
        return [doc["text"] for doc in self.load_documents()]
