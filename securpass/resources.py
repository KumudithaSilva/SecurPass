import os
from tkinter import PhotoImage

class ResourceLoader:
    def __init__(self, base_path=None):
        if base_path is None:
            base_path = os.path.join(os.path.dirname(__file__), "images")
        self.base_path = base_path

    def load_image(self, filename: str):
        path = os.path.join(self.base_path, filename)
        return PhotoImage(file=path) if os.path.exists(path) else None