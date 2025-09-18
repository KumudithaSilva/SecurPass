from securpass.ui import SecureUI
from securpass.config import Config
from securpass.messagebox import Messagebox


class Data_Retrieval:
    """
    Retrieval of the entry values .

    Attributes:
        ui: SecurePassUI instance to get entry values.
        config: Config instance containing default values.
        message (MessageBox): MessageBox instance to display messages.

    """

    def __init__(self, ui: SecureUI, config: Config, message: Messagebox):
        """
        Initialize the Data_Retrieval.

        Args:
            ui: SecurePassUI instance to get entry values.
            config: Config instance containing default values.
            message (MessageBox): MessageBox instance to display warnings.
        """
        self.ui = ui
        self.config = config
        self.message = message

    # --------------------------
    # Data Retrieval  Methods
    # --------------------------

    def ui_data_retrieval(self):
        """
        Retrieve website, email, and password from the UI.

        Returns:
            dict: Dictionary containing 'website', 'email', and 'password' keys.

        Raises:
            ValueError: If password is less than 10 characters.
        """
        website = self.ui.get_website()
        email = self.ui.get_email()
        password = self.ui.get_password()

        if len(password) < self.config.MIN_PASSWORD_LENGTH:
            self.message.show_warn(self.config.MSG_PASSWORD_TOO_SHORT)
            raise ValueError(self.config.MSG_PASSWORD_TOO_SHORT)

        data = {"website": website, "email": email, "password": password}
        return data
