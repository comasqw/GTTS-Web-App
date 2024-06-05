from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()

    lst_errors = []

    for error in errors:
        error_type = error["type"]

        if error_type == "enum":
            lst_errors.append("Language must be chosen between 'en'/'ru'")
        elif error_type == "string_too_short":
            lst_errors.append("Text must contain at least one character!")
        elif error_type == "string_too_long":
            lst_errors.append("Text must contain fewer than 500 characters!")
        elif error_type == "bool_parsing":
            lst_errors.append("The 'slow' value must be chosen between True/False")

    return JSONResponse(lst_errors, status_code=422)