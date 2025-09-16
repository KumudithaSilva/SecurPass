import csv
import os.path


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
        self.writer = csv.DictWriter(self.file, fieldnames=self.HEADERS)

        if os.path.getsize(self.filename) == 0:
            self.writer.writeheader()
            self.file.flush()

    # --------------------------
    # Data Save  Methods
    # --------------------------

    def data_save(self, data: dict):
        """
        Save website, email, and password to the CSV.

        Args:
            data (dict): Dictionary containing 'website', 'email', and 'password'.

        """
        self.writer.writerow(data)
        self.file.flush()

    def close(self):
        """Close the CSV file properly."""
        self.file.close()
