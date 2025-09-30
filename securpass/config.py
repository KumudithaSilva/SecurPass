class Config:
    """
    Configuration for SecurPass

    Attributes:
        EMAIL: Default email
        MIN_PASSWORD_LENGTH (int): Minimum required password length.
        MSG_PASSWORD_TOO_SHORT (str): Warning for short passwords.
        MSG_ENTRY_SAVED (str): Info message when entry is saved.
        MSG_ENTRY_CANCELLED (str): Info message when save is cancelled.
        MSG_CONFIRM_SAVE (str): Confirmation message template.

    """

    def __init__(self, email="kumudithasilva66@gmail.com", min_password_length=10):
        """
        Initialize Config with optional custom details.

        Args:
            email: Default user email
        """
        self.EMAIL = email
        self.MIN_PASSWORD_LENGTH = min_password_length
        self.MSG_PASSWORD_TOO_SHORT = "Password must be at least 10 characters"
        self.MSG_ENTRY_SAVED = "Entry saved successfully."
        self.MSG_ENTRY_CANCELLED = "Save operation cancelled."
        self.MSG_CONFIRM_SAVE = "Do you want to save the entry for: {}?"
        self.PASS_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.PASS_NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.PASS_SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
