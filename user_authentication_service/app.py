#!/usr/bin/env python3
"""this is the app.py file
"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/")
def welcome():
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def register_user():
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        
        AUTH.register_user(email, password)
        
        return jsonify({"email": email, "message": "user created"}), 200  # Set the status code to 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
