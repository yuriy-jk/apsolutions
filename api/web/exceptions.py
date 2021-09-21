class Error(Exception):
    status: int = 500
    code: str = "internal_error"
    description: str = "Internal Error"


class NotFound(Error):
    status = 404
    code = "not found"
    description = "Entity not found"
