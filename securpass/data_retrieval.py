from securpass.errors import PasswordTooShortError, EmptyWebsiteError
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
    # Get Website Name
    # --------------------------
    def get_website_name(self) -> str:
        """
        Retrieve the main part of the website name from the UI

        Returns:
            str: Base website name from UI
        """
        website_full = self.ui.get_website()
        website_name = website_full.split('.')[0]
        return website_name

    # --------------------------
    # Data Retrieval  Methods
    # --------------------------

    def ui_data_retrieval(self):
        """
        Retrieve website, email, and password from the UI and
        main part of the website name

        Returns:
            dict: Dictionary containing 'name', 'website', 'email', and 'password' keys.

        Raises:
            PasswordTooShortError: If password length is below configured minimum.
        """
        name = self.get_website_name()
        website = self.ui.get_website()
        email = self.ui.get_email()
        password = self.ui.get_password()

        if not website.strip():
            self.message.show_warn(self.config.EMPTY_WEBSITE)
            raise EmptyWebsiteError(self.config.EMPTY_WEBSITE)

        if len(password) < self.config.MIN_PASSWORD_LENGTH:
            self.message.show_warn(self.config.MSG_PASSWORD_TOO_SHORT)
            raise PasswordTooShortError(self.config.MSG_PASSWORD_TOO_SHORT)

        data = {"name": name, "website": website, "email": email, "password": password}
        return data
