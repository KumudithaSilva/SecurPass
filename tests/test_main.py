import unittest
from unittest.mock import MagicMock
from securpass.data_retrieval import Data_Retrieval


class TestDataRetrieval(unittest.TestCase):
    def setUp(self):
        # Create a mock UI
        self.mock_ui = MagicMock()
        self.mock_ui.get_website.return_value = "example.com"
        self.mock_ui.get_email.return_value = "user@example.com"
        self.mock_ui.get_password.return_value = "a" * 25

        self.data_retrieval = Data_Retrieval(self.mock_ui)

    def test_ui_data_retrieval(self):
        data = self.data_retrieval.ui_data_retrieval()
        self.assertEqual(data["website"], "example.com")
        self.assertEqual(data["email"], "user@example.com")
        self.assertEqual(data["password"], "a" * 25)

    def test_password_valid_length(self):
        test_valid_data = self.mock_ui.get_password.return_value = "abcdefghij@12"
        data = Data_Retrieval(self.mock_ui).ui_data_retrieval()
        self.assertEqual(data["password"], test_valid_data)

    def test_valid_password_length(self):
        self.mock_ui.get_password.return_value = "abcdefghij@12"
        data = self.data_retrieval.ui_data_retrieval()
        self.assertGreater(len(data["password"]), 10)

    def test_password_too_short_raises_error(self):
        self.mock_ui.get_password.return_value = "abc"
        with self.assertRaises(ValueError) as context:
            Data_Retrieval(self.mock_ui).ui_data_retrieval()
        self.assertEqual(
            str(context.exception), "Password must be at least 10 characters"
        )


if __name__ == "__main__":
    unittest.main()
