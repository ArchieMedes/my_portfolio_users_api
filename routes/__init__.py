"""
    Since this is a module, I will set what I need to map
    the routes for this module, importing them from "users_crud.py"
"""

# we need the module Blueprint from Flask for this
from flask import Blueprint


# Create a Blueprint fro the routes
users_blueprint = Blueprint('users', __name__)  # "__name__" is "routes"


# Import the routes from users_crud.py
"""
    We need to make the import here because
    "users_blueprint" is called from "users_crud.py" file,
    so, first it need to be created (line 11),
    and then, we import all what the "users_crud.py" says
"""
from .users_crud import *
