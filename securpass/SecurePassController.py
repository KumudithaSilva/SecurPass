from securpass.messagebox import Messagebox
from securpass.config import Config
from securpass.data_retrieval import Data_Retrieval
from securpass.data_save import Data_Saver
from securpass.password_generator import PasswordGenerator
from securpass.ui import SecureUI
import pyperclip


class SecurePassController:
    """
    Controller class that connects the UI,
    password generator, data retrieval, and data saving.

    Attributes:
        ui: SecureUI instance to interact with the user interface.
        config: Config instance containing default values.
        saver: DataSaver instance for saving retrieved data.
        retriever: DataRetrieval instance to fetch data from the UI.
        message (MessageBox): Instance to display confirmations and info.
        password: PasswordGenerator instance to generate password.
    """

    def __init__(
        self,
        ui: SecureUI,
        config: Config,
        saver: Data_Saver,
        retriever: Data_Retrieval,
        message: Messagebox,
        password: PasswordGenerator,
    ):
        """
        Initialize the SecurePassController.

        Args:
            ui: SecureUI instance to get entry values.
            config: Configuration instance.
            saver: DataSaver instance to save data.
            retriever: DataRetrieval instance to retrieve data from UI.
            message (MessageBox): Instance to display confirmations and info.
            password: PasswordGenerator Instance to generate passwords.
        """
        self.ui = ui
        self.config = config
        self.saver = saver
        self.retriever = retriever
        self.message = message
        self.password = password

        # Set default email in UI
        self.ui.set_email(self.config.EMAIL)

        # Wire the Generate Password and Add buttons to controller method
        self.ui.set_password_callback(self.generate_password)
        self.ui.set_add_callback(self.add_entry)

    def generate_password(self):
        """
        Generate a strong password, set it in the UI,
        and copy it to the system clipboard.
        """
        password = self.password.password_generation()
        self.ui.set_password(password)
        pyperclip.copy(password)

    def add_entry(self):
        """
        Retrieve data from UI entries, confirm saving,
        and save it if approved by the user.
        """
        data = self.retriever.ui_data_retrieval()
        website = data.get("website", "Unknown")

        if self.message.ask_confirmation(self.config.MSG_CONFIRM_SAVE.format(website)):
            self.saver.data_save(data)
            self.message.show_info(self.config.MSG_ENTRY_SAVED)
        else:
            self.message.show_info(self.config.MSG_ENTRY_CANCELLED)
