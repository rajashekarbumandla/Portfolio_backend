"""Error handling utilities."""
from flask import jsonify


def error_response(message, status_code=500, error_details=None):
    """
    Return a standardized JSON error response.

    Args:
        message (str): User-friendly error message
        status_code (int): HTTP status code
        error_details (str, optional): Additional error details

    Returns:
        tuple: (response dict, status code)
    """
    response = {
        "success": False,
        "error": message,
    }

    if error_details:
        response["details"] = error_details

    return jsonify(response), status_code


def success_response(data, message="Success"):
    """
    Return a standardized JSON success response.

    Args:
        data (list/dict): Response data
        message (str): Success message

    Returns:
        dict: Success response with data
    """
    return jsonify(
        {
            "success": True,
            "message": message,
            "data": data,
        }
    )
