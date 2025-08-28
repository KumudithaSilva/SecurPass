from tkinter import Canvas

class SecureUI:
    """
        A class to manage and display task-related UI components using Tkinter.

        Attributes:
            root (Tk): The main application window.
            images (dict): A dictionary containing Tkinter PhotoImage objects.
        """
    def __init__(self, root, images):
        self.root = root
        self.images = images

        # Canvas for main display
        self.canvas = Canvas(
            root,
            width=200,
            height=200,
            bg="#fdfdfd",
            highlightthickness=1
        )
        self.canvas.place(relx=0.5, y=10, anchor="n")

        # Initial logo images
        self.main_logo = self.canvas.create_image(100, 100, image=images["main_logo"])




