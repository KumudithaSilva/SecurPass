from tkinter import Tk
from securpass.resources import ResourceLoader
from securpass.ui import SecureUI


def main():
    root = Tk()
    root.title("SecurePass")
    root.geometry("250x250")
    root.config(padx=20, pady=20, bg="#fdfdfd")
    root.resizable(False, False)
    # root.iconbitmap("images/pasword-manager.ico")

    loader = ResourceLoader()
    images = {
        "main_logo": loader.load_image("securepass.png")
    }

    app = SecureUI(root, images)
    root.mainloop()


if __name__ == "__main__":
    main()


