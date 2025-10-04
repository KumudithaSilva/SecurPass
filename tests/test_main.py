import unittest
from unittest.mock import MagicMock
from securpass.data_retrieval import Data_Retrieval
from securpass.config import Config
from securpass.errors import PasswordTooShortError
from securpass.messagebox import Messagebox


class TestDataRetrieval(unittest.TestCase):
    def setUp(self):
        # Create a mock UI
        self.mock_ui = MagicMock()
        self.mock_ui.get_website.return_value = "example.com"
        self.mock_ui.get_email.return_value = "user@example.com"
        self.mock_ui.get_password.return_value = "a" * 25

        # Mock Config
        self.mock_config = MagicMock(spec=Config)
        self.mock_config.MIN_PASSWORD_LENGTH = 10
        self.mock_config.MSG_PASSWORD_TOO_SHORT = (
            "Password must be at least 10 characters"
        )
        self.mock_config.EMAIL = "user@example.com"

        # Mock Messagebox
        self.mock_message = MagicMock(spec=Messagebox)

        # Initialize Data_Retrieval with mocks
        self.data_retrieval = Data_Retrieval(
            ui=self.mock_ui, config=self.mock_config, message=self.mock_message
        )

    def test_ui_data_retrieval(self):
        data = self.data_retrieval.ui_data_retrieval()
        self.assertEqual(data["website"], "example.com")
        self.assertEqual(data["email"], "user@example.com")
        self.assertEqual(data["password"], "a" * 25)

    def test_password_valid_length(self):
        test_valid_data = self.mock_ui.get_password.return_value = "abcdefghij@12"
        data = self.data_retrieval.ui_data_retrieval()
        self.assertEqual(data["password"], test_valid_data)

    def test_valid_password_length(self):
        self.mock_ui.get_password.return_value = "abcdefghicj@9712"
        data = self.data_retrieval.ui_data_retrieval()
        self.assertGreater(len(data["password"]), 15)

    def test_password_too_short_raises_error(self):
        self.mock_ui.get_password.return_value = "abc"
        with self.assertRaises(PasswordTooShortError) as context:
            self.data_retrieval.ui_data_retrieval()
        self.assertEqual(
            str(context.exception), "Password must be at least 10 characters"
        )

    def test_password_too_short_shows_messagebox(self):
        self.mock_ui.get_password.return_value = "abc"
        with self.assertRaises(PasswordTooShortError):
            self.data_retrieval.ui_data_retrieval()
        self.mock_message.show_warn.assert_called_once_with(
            "Password must be at least 10 characters"
        )


if __name__ == "__main__":
    unittest.main()
