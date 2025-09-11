from securpass.ui import SecureUI


class Data_Retrieval:
    """
    Retrieval of the entry values .

    Attributes:
        ui: SecurePassUI instance to get entry values.

    """

    def __init__(self, ui: SecureUI):
        """
        Initialize the Data_Retrieval.

        Args:
            ui: SecurePassUI instance to get entry values.
        """
        self.ui = ui

    # --------------------------
    # Data Retrieval  Methods
    # --------------------------

    def ui_data_retrieval(self):
        """
        Retrieve website, email, and password from the UI.

        Returns:
            dict: Dictionary containing 'website', 'email', and 'password' keys.
        """
        website = self.ui.get_website()
        email = self.ui.get_email()
        password = self.ui.get_password()

        if len(password) < 10:
            raise ValueError("Password must be at least 10 characters")

        data = {"website": website, "email": email, "password": password}
        print(data)
        return data
