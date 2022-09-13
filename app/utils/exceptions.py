"""
Exceptions
"""


class APIException(Exception):
    """
    API Exception

    Attributes:
        system (str): The system having the issue (Ex: redis)
        status_code (int): The HTTP Status Code to return (Ex: 500)
        message (str): The error message to send with API response
    """

    def __init__(self, system: str, status_code: int, message: str) -> None:
        super().__init__(self)
        self.system = system
        self.status_code = status_code
        self.message = message
