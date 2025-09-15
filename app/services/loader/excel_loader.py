import pandas as pd
from typing import List
import os
from .universal_loader import UniversalLoader


class ExcelLoader(UniversalLoader):
    """
    Loader for Excel files.
    Extends UniversalLoader without modifying it (Open/Closed).
    """

    def _choose_loader(self):
        ext = os.path.splitext(self.file_path)[1].lower()
        if ext in [".xls", ".xlsx"]:
            return None
        else:
            return super()._choose_loader()

    def load_documents(self) -> List[dict]:
        """
        Load Excel rows as list of dicts with 'text' key instead of LangChain Document.
        """
        ext = os.path.splitext(self.file_path)[1].lower()
        if ext in [".xls", ".xlsx"]:
            df = pd.read_excel(self.file_path)
            texts = df.apply(lambda row: " ".join(map(str, row)), axis=1).tolist()
            return [{"text": text} for text in texts]
        else:
            return super().load_documents()

    def load_texts(self) -> List[str]:
        """
        Return list of row texts as strings.
        """
        documents = self.load_documents()
        return [doc["text"] for doc in documents]
