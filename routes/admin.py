"""
    Here we find all the routes for the SESSION api
    for the users of the platform
"""

# Third party imports
from flask import jsonify, Response

# Local imports
from utils.db import retrieve_all_users
from utils.exceptions import AllUsersDataError
from . import admin_blueprint  # Importing the pre-setting to map the routes inside the module


# PRIVATE ROUTES ==================================================
@admin_blueprint.route('/all', methods=['GET'])
def get_users():
    """
        Function to retrieve all the users registered,
        this will only be hitten by admin porpuses.
    """
    try:
        all_users = {
            "all_users": retrieve_all_users()
        }
        return Response(
            response=jsonify(all_users).get_data(),
            status=200,
            mimetype='application/json'
        )
    except AllUsersDataError as e:
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
