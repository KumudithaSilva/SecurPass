import os
from tkinter import PhotoImage


class ResourceLoader:
    def __init__(self, base_path=None):
        if base_path is None:
            base_path = os.path.join(os.path.dirname(__file__), "images")
        self.base_path = base_path

    def load_image(self, filename: str):
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found: {filename}")
        return PhotoImage(file=path)

    def load_icon(self, filename: str):
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Icon file not found: {filename}")
        return path