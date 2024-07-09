"""
Util functions to use across multiple
sections of the project related to
database queries
"""
# Third party libraries
from bson.objectid import ObjectId  # Importing ObjectId from bson library that comes with PyMongo
# Config imports
from config.db import mongo_instance  # First we need to make the connection to the database
from utils.exceptions import UserNotFoundError, AllUsersDataError


# =================================================================
def find_user_by_id(user_id):
    """
    Function to get the user
    by a given user_id
    """
    try:
        user_id = ObjectId(user_id)
        user_data = mongo_instance.db.users.find_one({"_id": user_id})
        if user_data is None:
            raise UserNotFoundError(f"User with id {user_id} not found")
        user_data["_id"] = str(user_data["_id"])
        return user_data
    except UserNotFoundError as unf:
        raise unf
    except Exception as e:
        print("general exception at find_user_by_id:", e)
        raise e


def retrieve_all_users():
    """
    Function to retrieve all users registered in the database
    """
    try:
        all_users = mongo_instance.db.users.find()
        all_users = list(all_users)
        if not all_users or all_users is None:
            raise AllUsersDataError("Users were not found in collection")
        return [convert_objectid_to_str(user) for user in all_users ]
    except AllUsersDataError as all_users_error:
        raise all_users_error
    except Exception as e:
        raise e


def convert_objectid_to_str(doc):
    """Util function to convert an objectid into a string"""
    if '_id' in doc:
        doc["_id"] = str(doc["_id"])
    return doc


def register_user(user_data):
    # Now we will try to store the new user in db
    print("user_data:", user_data)
    db_response = mongo_instance.db.users.insert_one(user_data)  # 'users' is a collection inside 'users_db'
    print('db_response:', db_response)
    return {
        'result': 'success',
        'document_id': str(db_response.inserted_id)
    }
