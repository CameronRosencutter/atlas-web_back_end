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


# New error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized_error(error):
    """Reports back if an unauthorized error occurs"""
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response


# Blueprint registration
app.register_blueprint(index)

if __name__ == '__main__':
    app.run(debug=True)


# Import the views blueprint
from api.v1.views.index import bp as views_bp

# Register the views blueprint
app.register_blueprint(views_bp)

# Custom error handler for 401
@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401
