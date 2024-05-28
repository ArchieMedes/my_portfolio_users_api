"""
    This the main app for
    my portfolio users API
"""
# IMPORTS ============================================================================
from flask import Flask

# CONFIG IMPORTS
from config.db import init_db

# NATIVE IMPORTS
from routes import users_blueprint


# SETTING ============================================================================
app = Flask(__name__)

# Database configuration
# 'mongo-db' is the service name in docker compose
app.config["MONGO_URI"] = "mongodb://mongo-db:27017/users_db"
init_db(app)  # Initialize MongoDB with the Flask app

# Register the users routes Blueprint
app.register_blueprint(users_blueprint, url_prefix='/api')


# HEALTH CHECK =======================================================================
@app.route("/")
def hello_world():
    """ just a health check"""
    return "<p>Hello World!</p>"
