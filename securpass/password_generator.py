import random

from securpass.config import Config


class PasswordGenerator:
    """
     Generates strong password using letters, numbers, and symbols.

    Attributes:
        config (Config): Configuration object holding password character sets.
        letters (str): String of allowed letters.
        numbers (str): String of allowed digits.
        symbols (str): String of allowed symbols.
        password (list): List used to build the password.
        generated_password (str): The final generated password.
        letters_length (int): Number of letters in the password.
        numbers_length (int): Number of numbers in the password.
        symbols_length (int): Number of symbols in the password.
    """
    def __init__(self, config: Config):
        """
        Initialize the PasswordGenerator with provided configuration.

        Args:
            config (Config): Config instance containing default character sets.
        """
        self.config = config

        self.letters = self.config.PASS_LETTERS
        self.numbers = self.config.PASS_NUMBERS
        self.symbols = self.config.PASS_SYMBOLS

        self.password: list[str] = []
        self.generated_password: str | None = None

        self.letters_length : int = random.randint(8, 10)
        self.numbers_length : int = random.randint(2, 4)
        self.symbols_length : int = random.randint(2, 4)


    # -----------------------------
    # Password Generation  Methods
    # ----------------------------

    def password_generation(self) -> str:
        """
        Generate a strong random password.

        The password will include:
        - 8–10 random letters
        - 2–4 random numbers
        - 2–4 random symbols

        Returns:
            str: The generated password.
        """
        self.password = []

        for char in range(self.letters_length):
            self.password.append(random.choice(self.letters))

        for char in range(self.numbers_length):
            self.password.append(random.choice(self.numbers))

        for char in range(self.symbols_length):
            self.password.append(random.choice(self.symbols))

        random.shuffle(self.password)
        self.generated_password = "".join(self.password)

        return self.generated_password
