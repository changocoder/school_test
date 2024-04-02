from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    def __init__(self, message, status_code=400):
        super().__init__(description=message)
        self.code = status_code


class NotFoundException(APIException):
    def __init__(self, message="Resource not found"):
        super().__init__(message, 404)


class BadRequestException(APIException):
    def __init__(self, message="Bad request"):
        super().__init__(message, 400)


class InternalServerErrorException(APIException):
    def __init__(self, message="Internal server error"):
        super().__init__(message, 500)


class FilterException(APIException):
    def __init__(self, message="Error in filter operation"):
        super().__init__(message, 400)
