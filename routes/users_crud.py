"""
    Here we find all the routes for the CRUD api
    for the users of the platform
"""

# Third party imports
from flask import request, jsonify

# Config imports
from config.db import mongo_instance

# Local imports
from . import users_blueprint  # Importing the pre-setting to map the routes inside the module


# ROUTES ========================================================
@users_blueprint.route('/user/sign-up', methods=['POST'])
def sign_up():
    """
        This function is for registering any new user
        at a time (CREATE)
    """

    user_data = request.json
    if not user_data:  # To validate the existence of actual data in the request payload
        return jsonify({'error': 'Missing payload data'}), 400

    # Now we will try to store the new user in db
    db_response = mongo_instance.db.users.insert_one(user_data)  # 'users' is a collection inside 'users_db'
    print('db_response:', db_response)

    return jsonify({
        'result': 'success',
        'document_id': str(db_response.inserted_id)
    }), 201


@users_blueprint.route('/user/log-in', methods=['PUT'])
def log_in():
    """
        This function is for log-in an user
    """

    return "Inicio de sesion"


@users_blueprint.route('/user/log-out/<int:user_id>', methods=['PUT'])
def log_out(user_id):
    """
        This function is for log-out an user
    """

    return f"Cierre de sesion del usuario {user_id}"


@users_blueprint.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
        Function to retrieve a specific user data
    """

    return f"User {user_id}"


@users_blueprint.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
        Function to update data for a specific user
    """

    return f"User {user_id} updated!"


@users_blueprint.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
        Function to delete a specific user account
    """

    return f"User {user_id} deleted!"


# PRIVATE ROUTES ==================================================
@users_blueprint.route('/user/all', methods=['GET'])
def get_users():
    """
        Function to retrieve all the users registered,
        this will only be hitten by admin porpuses.
    """

    return "List of all users"