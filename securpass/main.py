from tkinter import Tk
from securpass.config import Config
from securpass.data_retrieval import Data_Retrieval
from securpass.resources import ResourceLoader
from securpass.ui import SecureUI


def main():
    root = Tk()
    loader = ResourceLoader()
    images = {
        "main_logo": loader.load_image("securepass.png"),
        "main_icon": loader.get_resource_path("securepass.ico"),
    }

    # Load configuration
    config = Config()

    # Initialize UI
    ui = SecureUI(root, images)
    ui.set_email(config.EMAIL)

    # Initialize data retrieval and attach callback
    data_retrieval = Data_Retrieval(ui)
    ui.set_add_callback(data_retrieval.ui_data_retrieval)

    root.mainloop()


if __name__ == "__main__":
    main()
