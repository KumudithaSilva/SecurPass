class Data_Saver:
    """
    Save the entry values to CSV .

    Attributes:
        filename (str): Path to the CSV file where data will be stored.
        file: Open file object.
        writer: DictWriter object.

    """

    HEADERS = ["website", "email", "password"]

    def __init__(self, filename: str = "data.csv"):
        """
        Initialize the Data_Saver.

        Args:
            filename (str): Path to the CSV file where data will be stored.
        """
        self.filename = filename
        self.file = open(self.filename, mode="a", newline="", encoding="utf-8")

        if self.file.tell() == 0:
            self.file.write(" | ".join(self.HEADERS) + "\n")

    # --------------------------
    # Data Save  Methods
    # --------------------------

    def data_save(self, data: dict):
        """
        Save website, email, and password to the CSV.

        Args:
            data (dict): Dictionary containing 'website', 'email', and 'password'.

        """
        row = " | ".join(data[h] for h in self.HEADERS)
        self.file.write(row + "\n")
        self.file.flush()

    def close(self):
        """Close the CSV file properly."""
        self.file.close()
