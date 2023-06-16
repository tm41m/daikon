from functools import wraps
from flask import request, jsonify


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = request.headers.get('Authorization')

        # Check if auth token is valid (add your validation logic here)
        if auth_token == 'valid_token':
            # Token is valid, proceed with the decorated function
            return f(*args, **kwargs)
        else:
            # Token is invalid, return an error response
            response = jsonify({'message': 'Invalid authentication token'})
            response.status_code = 401  # Unauthorized
            return response

    return decorated
