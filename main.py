from tkinter import Tk
from securpass.resources import ResourceLoader
from securpass.ui import SecureUI


def main():
    root = Tk()
    loader = ResourceLoader()
    images = {
        "main_logo": loader.load_image("securepass.png"),
        "main_icon": loader.load_icon("securepass.ico")
    }
    app = SecureUI(root, images)
    root.mainloop()


if __name__ == "__main__":
    main()

