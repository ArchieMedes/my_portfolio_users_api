"""
    Here we find all the routes for the SESSION api
    for the users of the platform
"""

# Third party imports
from flask import request, jsonify, Response

# Config imports
from config.db import mongo_instance

# Local importssession_blueprint
from utils.exceptions import MissingPayloadData
from utils.db import register_user
from . import session_blueprint  # Importing the pre-setting to map the routes inside the module


# ROUTES ==================================================
@session_blueprint.route('/sign-up', methods=['POST'])
def sign_up():
    """
        This function is for registering any new user
        at a time (CREATE)
    """
    try:
        user_data = request.json
        if not user_data:  # To validate the existence of actual data in the request payload
            raise MissingPayloadData('Missing payload data')
        registered_user = register_user(user_data)
        print("Registered user:", registered_user)
        return Response(
            response=jsonify(registered_user).get_data(),
            status=201,
            mimetype='application/json'
        )
    except MissingPayloadData as msg:
        return Response(
            response=jsonify({
                "error": str(msg)
            }).get_data(),
            status=400,
            mimetype='application/json'
        )
    except Exception as e:
        return Response(
            response=jsonify({
                "error": e
            }).get_data(),
            status=500,
            mimetype='application/json'
        )

@session_blueprint.route('/log-in', methods=['PUT'])
def log_in():
    """
        This function is for log-in an user
    """

    return "Inicio de sesion"


@session_blueprint.route('/log-out/<user_id>', methods=['PUT'])
def log_out(user_id):
    """
        This function is for log-out an user
    """

    return f"Cierre de sesion del usuario {user_id}"
