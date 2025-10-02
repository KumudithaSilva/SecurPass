import  json
import os.path

class Data_Saver:

    """
    Save website, email, and password entries to a JSON file.

    Attributes:
        filename (str): Path to the JSON file where data will be stored.
    """

    def __init__(self, filename = "data.json"):
        """
        Initialize the Data_Saver.

        Args:
            filename (str): Path to the JSON file where data will be stored.
        """
        self.filename = filename
        if not os.path.isfile(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file)

    # --------------------------
    # Data Save  Methods
    # --------------------------

    def data_save(self, data: dict):
        """
        Save website, email, and password to the JSON file.

        Args:
            data (dict): Dictionary containing 'website', 'email', and 'password'.
        """
        with open(self.filename, "r+", encoding="utf-8") as file:
            existing_data = json.load(file)
            existing_data.append(data)
            file.seek(0)
            json.dump(existing_data, file, indent=4)
            file.truncate()

    # --------------------------
    # Data Read  Methods
    # --------------------------

    def data_read(self):
        """
        Retrieve website, email, and password from the JSON file.

        Returns:
            dict: Dictionary containing 'website', 'email', and 'password' keys.
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(data)
            return data