import os
from typing import Dict, Callable
from .file_type import FileType


class FileTypeRegistry:
    """
    Registry only responsible for storing mapping of FileType -> loader factory.
    """

    _registry: Dict[FileType, Callable[[str], object]] = {}

    @classmethod
    def register(cls, file_type: FileType, loader_factory: Callable[[str], object]):
        cls._registry[file_type] = loader_factory

    @classmethod
    def get_loader(cls, file_path: str):
        """Return loader instance based on file extension."""
        ext = os.path.splitext(file_path)[1].lower()
        for file_type, factory in cls._registry.items():
            if file_type.value == ext:
                return factory(file_path)
        raise ValueError(f"Unsupported file type: {ext}")
