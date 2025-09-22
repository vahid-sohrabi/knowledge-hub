import os
from fastapi import UploadFile

class FileHandler:
    """
    Utility class for handling temporary file operations.
    This is generic and not tied to business logic (utils instead of services).
    """

    def __init__(self, base_dir: str = "."):
        self.base_dir = base_dir

    async def save_temp(self, file: UploadFile) -> str:
        """
        Saves an uploaded file temporarily and returns its path.
        """
        temp_path = os.path.join(self.base_dir, f"temp_{file.filename}")
        file_bytes = await file.read()
        with open(temp_path, "wb") as f:
            f.write(file_bytes)
        return temp_path

    def delete(self, path: str):
        """
        Deletes a file if it exists.
        """
        if os.path.exists(path):
            os.remove(path)
