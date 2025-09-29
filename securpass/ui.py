from tkinter import Canvas, Label, Entry, Button, Tk


class SecureUI:
    """
    A professional Tkinter-based UI for SecurePass.

    Responsibilities:
        - Render all UI elements: logo canvas, entries, buttons
        - Expose public API for retrieving and setting entry values
        - Allow setting callback for the Add button

    Attributes:
        _root (Tk): Main Tkinter application window.
        _images (dict): Dictionary of Tkinter PhotoImage objects.
        _canvas (Canvas): Canvas for logo or graphics.
        _website_entry (Entry): Entry widget for website.
        _email_entry (Entry): Entry widget for email/username.
        _password_entry (Entry): Entry widget for password.
        _add_button (Button): Button to submit the data.
        _generate_password (Button): Button to generate a password.
    """

    BG_COLOR = "#F5F7FA"
    FONT_COLOUR = "#1E1E1E"
    LABEL_COLOUR = "#F5F7FA"
    LABEL_FONT_COLOUR = "#1E1E1E"
    ENTRY_COLOUR = "#FFFFFF"
    PRIMARY_BUTTON_COLOUR = "#4ADEA6"
    SECONDARY_BUTTON_COLOUR = "#2E3D3D"
    LABEL_FONT = ("Segoe UI", 10, "bold")

    FIELD_WIDTH = 45

    def __init__(self, root: Tk, images=None, add_callback=None, pass_callback= None):
        """
        Initialize the SecureUI.

        Args:
            root (Tk): The main Tkinter window.
            images (dict, optional): Dictionary containing 'main_logo' and 'main_icon'.
            add_callback (callable, optional): Function to call when Add button is clicked.
            pass_callback (Callable, optional): Function called when Generate button is clicked.
        """
        self._root = root
        self._images = images or {}

        # Declare attributes upfront for clarity & avoid attribute errors
        self._canvas = None
        self._website_entry = None
        self._email_entry = None
        self._password_entry = None
        self._add_button = None
        self._generate_password = None

        # Build the UI
        self._build_ui()

        # Wire callbacks after widgets are created
        if add_callback:
            self.set_add_callback(add_callback)
        if pass_callback:
            self.set_password_callback(pass_callback)

    def _build_ui(self):
        """UI widgets and layout."""

        # Window configuration
        self._root.title("SecurePass")
        self._root.config(padx=40, pady=40, bg=self.BG_COLOR)
        self._root.resizable(False, False)

        # Set application icon if provided
        if "main_icon" in self._images:
            self._root.iconbitmap(self._images["main_icon"])

        # Apply global styles
        self._root.option_add("*Label.Background", self.LABEL_COLOUR)
        self._root.option_add("*Entry.Background", self.ENTRY_COLOUR)

        # Canvas for logo
        self._canvas = Canvas(
            self._root, width=200, height=200, bg=self.BG_COLOR, highlightthickness=0
        )
        if "main_logo" in self._images:
            self._canvas.create_image(100, 100, image=self._images["main_logo"])
        self._canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Website Entry
        Label(text="Website:", fg=self.LABEL_FONT_COLOUR, font=self.LABEL_FONT).grid(
            row=1, column=0, sticky="e", pady=5, padx=(0, 10)
        )
        self._website_entry = Entry(
            width=self.FIELD_WIDTH, highlightthickness=0, relief="ridge"
        )
        self._website_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
        self._website_entry.focus()  # Focus on website entry initially

        # Email Entry
        Label(
            text="Email/Username:", fg=self.LABEL_FONT_COLOUR, font=self.LABEL_FONT
        ).grid(row=2, column=0, sticky="e", pady=5, padx=(0, 10))
        self._email_entry = Entry(
            width=self.FIELD_WIDTH, highlightthickness=0, relief="ridge"
        )
        self._email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="n")

        # Password Entry
        Label(text="Password:", fg=self.LABEL_FONT_COLOUR, font=self.LABEL_FONT).grid(
            row=3, column=0, sticky="e", pady=5, padx=(0, 10)
        )
        self._password_entry = Entry(width=23, highlightthickness=0, relief="ridge")
        self._password_entry.grid(row=3, column=1, pady=5, sticky="w")

        # Generate Password Button
        self._generate_password = Button(
            text="Generate Password",
            width=15,
            highlightthickness=0,
            relief="ridge",
            bg=self.PRIMARY_BUTTON_COLOUR,
            fg=self.FONT_COLOUR,
        )
        self._generate_password.grid(
            row=3, column=2, sticky="w", columnspan=2, padx=(0, 2)
        )

        # Add Button
        self._add_button = Button(
            text="Add",
            width=38,
            highlightthickness=0,
            relief="ridge",
            bg=self.PRIMARY_BUTTON_COLOUR,
            fg=self.FONT_COLOUR,
        )
        self._add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=10)

    # -----------------------------
    # Public getters
    # -----------------------------
    def get_website(self) -> str:
        """Return the current value of the website entry."""
        return self._website_entry.get()

    def get_email(self) -> str:
        """Return the current value of the email entry."""
        return self._email_entry.get()

    def get_password(self) -> str:
        """Return the current value of the password entry."""
        return self._password_entry.get()

    # -----------------------------
    # Public setters
    # -----------------------------
    def set_website(self, website: str):
        """Set the website entry value."""
        self._website_entry.delete(0, "end")
        self._website_entry.insert(0, website)

    def set_email(self, email: str):
        """Set the email entry value."""
        self._email_entry.delete(0, "end")
        self._email_entry.insert(0, email)

    def set_password(self, password: str):
        """Set the password entry value."""
        self._password_entry.delete(0, "end")
        self._password_entry.insert(0, password)

    # -----------------------------
    # Public method to set button callback dynamically
    # -----------------------------
    def set_add_callback(self, callback):
        """
        Set or update the Add button callback.

        Args:
            callback (callable): Function to call when the Add button is clicked.
        """
        self._add_button.config(command=callback)

    # -----------------------------
    # Public method to generate password when button callback dynamically
    # -----------------------------
    def set_password_callback(self, callback):
        """
        Set or update the Generate button callback.

        Args:
            callback (callable): Function to call when Generate button is clicked.
        """
        self._generate_password.config(command=callback)
