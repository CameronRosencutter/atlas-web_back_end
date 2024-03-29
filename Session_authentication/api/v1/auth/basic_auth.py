#!/usr/bin/env python3
"""
basic_auth
"""


from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class (inherits from Auth) """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
            self, base_64_authorization_header: str) -> str:
        """
        Decodes the Base64 Authorization header
        """
        if base_64_authorization_header is None or \
                not isinstance(base_64_authorization_header, str):
            return None

        try:
            decode_bytes = base64.b64decode(base_64_authorization_header)
            decode_str = decode_bytes.decode('utf-8')
            return decode_str
        except base64.biascii.Error:
            return None
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
                self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on user email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
