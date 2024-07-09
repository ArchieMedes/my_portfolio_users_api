"""
    Here we find all the routes for the CRUD api
    for the users of the platform
"""

# Third party imports
from flask import request, jsonify, Response

# Local imports
from utils.db import find_user_by_id
from utils.exceptions import UserNotFoundError
from . import users_blueprint  # Importing the pre-setting to map the routes inside the module


# ROUTES ========================================================
@users_blueprint.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """
        Function to retrieve a specific user data
    """
    try:
        user_data = find_user_by_id(user_id)
        return Response(
            response=jsonify(user_data).get_data(),
            status=200,
            mimetype='application/json'
        )
    except UserNotFoundError as e:
        return Response(
            response=jsonify({"error": str(e)}).get_data(),
            status=404,
            mimetype='application/json'
        )
    except Exception as e:
        return Response(
            response=jsonify({"error": str(e)}).get_data(),
            status=500,
            mimetype='application/json'
        )


@users_blueprint.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
        Function to update data for a specific user
    """

    return f"User {user_id} updated!"


@users_blueprint.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
        Function to delete a specific user account
    """

    return f"User {user_id} deleted!"
