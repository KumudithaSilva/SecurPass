from tkinter import Canvas, Label, Entry, Button


class SecureUI:
    """
        A class to manage and display task-related UI components using Tkinter.

        Attributes:
            root (Tk): The main application window.
            images (dict): A dictionary containing Tkinter PhotoImage objects.
        """
    BG_COLOR = "#ffffff"
    FIELD_WIDTH = 45

    def __init__(self, root, images):
        self.root = root
        self.images = images

        # Main Screen
        self.root.title("SecurePass")
        self.root.config(padx=40, pady=40, bg=self.BG_COLOR)
        self.root.resizable(False, False)
        self.root.iconbitmap(images["main_icon"])

        # Apply global styles
        self.root.option_add("*Label.Background", self.BG_COLOR)
        self.root.option_add("*Entry.Background", self.BG_COLOR)
        self.root.option_add("*Button.Background", self.BG_COLOR)

        # Canvas for logo
        self.canvas = Canvas(
            root,
            width=200,
            height=200,
            bg=self.BG_COLOR,
            highlightthickness=0
        )
        self.canvas.create_image(100, 100, image=images["main_logo"])
        self.canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Labels & Entries
        Label(text="Website:").grid(row=1, column=0, sticky="e", pady=5, padx=(0, 10))
        self.website_entry = Entry(width=45, highlightthickness=0, relief="ridge")
        self.website_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")

        Label(text="Email/Username:").grid(row=2, column=0, sticky="e", pady=5, padx=(0, 10))
        self.email_entry = Entry(width=45, highlightthickness=0, relief="ridge")
        self.email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="n")

        Label(text="Password:").grid(row=3, column=0, sticky="e", pady=5, padx=(0, 10))
        self.password_entry = Entry(width=21, highlightthickness=0, relief="ridge")
        self.password_entry.grid(row=3, column=1, pady=5, sticky="w")

        # Buttons
        self.generate_password = Button(text="Generate Password", width=15, highlightthickness=0, relief="ridge")
        self.generate_password.grid(row=3, column=2, sticky="w",columnspan=2, padx=(0, 2))

        self.add_button = Button(text="Add", width=38, highlightthickness=0, relief="ridge")
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=10)
