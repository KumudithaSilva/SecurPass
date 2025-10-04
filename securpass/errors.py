class SecurPassError(Exception):
    """Base class for all SecurPass-specific exceptions"""

    pass


# Password-related errors
class WeakPasswordError(SecurPassError):
    pass


class PasswordTooShortError(SecurPassError):
    pass


# File & Storage errors
class DataFileNotFoundError(SecurPassError):
    pass


class DataCorruptionError(SecurPassError):
    pass


# Security errors
class EncryptionError(SecurPassError):
    pass


class DecryptionError(SecurPassError):
    pass


# Website
class EmptyWebsiteError(SecurPassError):
    pass
