from securpass.messagebox import Messagebox
from securpass.config import Config
from securpass.data_retrieval import Data_Retrieval
from securpass.data_save import Data_Saver
from securpass.ui import SecureUI


class SecurePassController:
    """
    Controller class that connects UI, data retrieval, and data saving.

    Attributes:
        ui: SecureUI instance to interact with the user interface.
        config: Config instance containing default values.
        saver: DataSaver instance for saving retrieved data.
        retriever: DataRetrieval instance to fetch data from the UI.
        message (MessageBox): Instance to display confirmations and info.
    """

    def __init__(
        self,
        ui: SecureUI,
        config: Config,
        saver: Data_Saver,
        retriever: Data_Retrieval,
        message: Messagebox,
    ):
        """
        Initialize the SecurePassController.

        Args:
            ui: SecureUI instance to get entry values.
            config: Config instance containing default values.
            saver: DataSaver instance to save data.
            retriever: DataRetrieval instance to retrieve data from UI.
            message (MessageBox): Instance to display confirmations and info.
        """
        self.ui = ui
        self.config = config
        self.saver = saver
        self.retriever: Data_Retrieval = retriever
        self.message = message

        # Set default email in UI
        self.ui.set_email(self.config.EMAIL)

        # Wire the Add button to controller method
        self.ui.set_add_callback(self.add_entry)

    def add_entry(self):
        """Retrieve data from UI and save it."""
        data = self.retriever.ui_data_retrieval()
        website = data.get("website", "Unknown")

        if self.message.ask_confirmation(self.config.MSG_CONFIRM_SAVE.format(website)):
            self.saver.data_save(data)
            self.message.show_info(self.config.MSG_ENTRY_SAVED)
        else:
            self.message.show_info(self.config.MSG_ENTRY_CANCELLED)
