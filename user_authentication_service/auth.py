#!/usr/bin/env python3
"""this is the auth.py file
"""

from db import DB
from user import User  # Assuming you have a User class defined
import bcrypt

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """This is the init function"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """This will register user in the system"""
        # Check if the user already exists with the given email
        existing_user = self._db.get_user_by_email(email)
        if existing_user:
            raise ValueError(f"User {email} already exists.")

        # Hash the password using bcrypt
        hashed_password = self._hash_password(password)

        # Create a new User object
        new_user = User(email, hashed_password)

        # Save the user to the database
        self._db.save_user(new_user)

        # Return the User object
        return new_user

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """This will hide and limit the password"""
        # Hash the password using bcrypt
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Assuming you have a User class defined with an appropriate __init__ method
