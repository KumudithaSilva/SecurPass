import json
import os.path
from errors import DataFileNotFoundError, DataCorruptionError


class Data_Saver:
    """
    Save website, email, and password entries to a JSON file.

    Attributes:
        filename (str): Path to the JSON file where data will be stored.
    """

    def __init__(self, filename="data.json"):
        """
        Initialize the Data_Saver.

        Args:

            filename (str): Path to the JSON file where data will be stored.
        """
        self.filename = filename

        if not os.path.isfile(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump({}, file)

    # --------------------------
    # Data Save  Methods
    # --------------------------

    def data_save(self, data: dict):
        """
        Save website, email, and password to the JSON file.

        Args:
            data (dict): Dictionary containing 'website', 'email', and 'password'.
        """
        try:
            with open(self.filename, "r+", encoding="utf-8") as file:
                try:
                    existing_data = json.load(file)
                    if not isinstance(existing_data, dict):
                        raise DataCorruptionError(
                            f"Data file {self.filename} is corrupted."
                        )
                except json.JSONDecodeError as e:
                    raise DataCorruptionError(
                        f"JSON corrupted in {self.filename}"
                    ) from e

                website_name = data['name']
                existing_data[website_name] = {
                    "website": data["website"],
                    "email": data["email"],
                    "password": data["password"],
                }

                file.seek(0)
                json.dump(existing_data, file, indent=4)
                file.truncate()

        except FileNotFoundError as e:
            raise DataFileNotFoundError(f"File not found: {self.filename}") from e

    # --------------------------
    # Data Read  Methods
    # --------------------------

    def data_read(self):
        """
        Retrieve website, email, and password from the JSON file.

        Returns:
            dict: Dictionary containing 'website', 'email', and 'password' keys.
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, dict):
                        raise DataCorruptionError(
                            f"Data file {self.filename} is corrupted."
                        )
                    return data
                except json.JSONDecodeError as e:
                    raise DataCorruptionError(
                        f"JSON corrupted in {self.filename}"
                    ) from e
        except FileNotFoundError as e:
            raise DataFileNotFoundError(f"File not found: {self.filename}") from e
