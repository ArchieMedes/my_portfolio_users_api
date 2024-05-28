"""
    Here yu will find the configuration
    for the MongoDB database that this API is using
"""
# IMPORTS ============================================================================
from flask_pymongo import PyMongo


# =================================================================
mongo_instance = PyMongo()


# =================================================================
def init_db(app):
    """ initialize the database"""
    mongo_instance.init_app(app)
