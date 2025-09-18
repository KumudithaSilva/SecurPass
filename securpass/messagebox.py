from tkinter import messagebox


class Messagebox:
    """
    Wrapper class for displaying confirmation, info dialogs and warring.

    Attributes:
        title (str): Title of the message box window.
    """

    def __init__(self, title: str = "SecurePass"):
        """
        Initialize the MessageBox with a default title.

        Args:
            title (str, optional): Title of the message box. Defaults to "SecurePass".
        """
        self.title = title

    def ask_confirmation(self, message: str) -> bool:
        """
        Display a confirmation dialog with OK/Cancel buttons.

        Args:
            message (str): Message to display in the dialog.

        Returns:
            bool: True if user clicks OK, False if user clicks Cancel.
        """
        return messagebox.askokcancel(title=self.title, message=message)

    def show_info(self, message: str):
        """
        Display an information dialog with OK button.
        """
        messagebox.showinfo(title=self.title, message=message)

    def show_warn(self, message: str):
        """
        Display warning dialog.
        """
        messagebox.showwarning(title=self.title, message=message)
