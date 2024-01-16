#!/usr/bin/env python3
"""Route module for the API"""

from flask import Flask, jsonify
from api.v1.views import index

app = Flask(__name__)

# Existing routes and configurations...

# New error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized_error(error):
    """reports back if an unauthorized error occurs"""
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response

# Blueprint registration
app.register_blueprint(index)

if __name__ == '__main__':
    app.run(debug=True)
