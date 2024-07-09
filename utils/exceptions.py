
"""
Files for exceptions definitions
"""


# =================================================================
class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the database."""


class AllUsersDataError(Exception):
    """Exception raised when is not possible to get all users registered from DB"""


class MissingPayloadData(Exception):
    """Exception raised when is not possible to register a user"""
