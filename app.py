"""
    This the main app for
    my portfolio users API
"""
# IMPORTS ============================================================================
from flask import Flask
from routes import users_blueprint


# SETTING ============================================================================
app = Flask(__name__)

# Register the users Blueprint
app.register_blueprint(users_blueprint, url_prefix='/api')


# HEALTH CHECK =======================================================================
@app.route("/")
def hello_world():
    """ just a health check"""
    return "<p>Hello World!</p>"
