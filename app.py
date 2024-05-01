"""
    This the main app for
    my portfolio users API
"""
# IMPORTS ======================================
from flask import Flask


# SETTING ======================================
app = Flask(__name__)


# HEALTH CHECK =================================
@app.route("/")
def hello_world():
    """ just a health check"""
    return "<p>Hello World!</p>"
