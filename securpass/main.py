from tkinter import Tk

from securpass.SecurePassController import SecurePassController
from securpass.config import Config
from securpass.data_retrieval import Data_Retrieval
from securpass.data_save import Data_Saver
from securpass.messagebox import Messagebox
from securpass.resources import ResourceLoader
from securpass.ui import SecureUI


def main():
    root = Tk()
    loader = ResourceLoader()
    images = {
        "main_logo": loader.load_image("securepass.png"),
        "main_icon": loader.get_resource_path("securepass.ico"),
    }

    ui = SecureUI(root, images)
    config = Config()
    saver = Data_Saver()
    messagebox = Messagebox()
    retriever = Data_Retrieval(ui, config, messagebox)

    SecurePassController(ui, config, saver, retriever, messagebox)

    root.mainloop()
    saver.close()


if __name__ == "__main__":
    main()
