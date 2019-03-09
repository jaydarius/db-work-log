class Error(Exception):
   """Base class for other exceptions"""
   pass

class InvalidDate(Error):
    """Raised when date is invalid"""
    pass

class InvalidUser(Error):
    """Raised when user is invalid"""
    pass

class InvalidTime(Error):
    """Raised when time is invalid"""
    pass

class InvalidTitle(Error):
    """Raised when title is invalid"""
    pass

class InvalidKeyword(Error):
    """Raised when keyword is invalid"""
    pass