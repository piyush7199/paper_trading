from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        error_message = ""
        if isinstance(response.data, dict):
            error_message = ", ".join([f"{k}: {v[0]}" for k, v in response.data.items()])
        elif isinstance(response.data, list):
            error_message = ", ".join(response.data)
        else:
            error_message = str(response.data)

        response.data = {
            "status": "error",
            "error": error_message
        }

    return response