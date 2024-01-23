#!/usr/bin/env python3
"""this is the auth.py file
"""

from db import DB
from user import User  # Assuming you have a User class defined

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """This is where the inut is
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            User: _description_
        """
        # Check if the user already exists with the given email
        existing_user = self._db.get_user_by_email(email)
        if existing_user:
            raise ValueError(f"User {email} already exists.")

        # Hash the password using your _hash_password method
        hashed_password = self._hash_password(password)

        # Create a new User object
        new_user = User(email, hashed_password)

        # Save the user to the database
        self._db.save_user(new_user)

        # Return the User object
        return new_user

    def _hash_password(self, password: str) -> bytes:
        """This is the hashpassword

        Args:
            password (str): password is a string

        Returns:
            bytes: This has bytes in it
        """
        # Implement your _hash_password method here (similar to the previous example)
        # ...

# Assuming you have a User class defined with an appropriate __init__ method
