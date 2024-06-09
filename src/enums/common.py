from enum import Enum



class Status(Enum):
    """"
    This is all get statuses
    """
    Available: str = "available"
    NotAvailable: str = "not-vailable"




class HttpErrorCodes(Enum):
    Content: int = 200
    BadRequest: int = 400
    NotFound: int = 404
