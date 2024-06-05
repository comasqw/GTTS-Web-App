from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="temp")

def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()

    lst_errors = []

    for error in errors:
        lst_errors.append([error["type"], error["loc"]])

    return templates.TemplateResponse("invalid_value.html", {"request": request,
                                                    "errors": lst_errors})