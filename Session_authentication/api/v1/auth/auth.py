#!/usr/bin/env python3
'''This is the auth.py file in use'''
from flask import request
from typing import List
from typing import TypeVar
import os


class Auth():
    '''For the Author of this file'''

    def __init__(self) -> None:
        '''This is just for the init'''

    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        '''For the Required authority'''
        if path is None:
            # print('path is None')
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            # print("excluded paths is None or empty")
            return True
        elif path in excluded_paths:
            # print('path is in excluded paths')
            return False
        elif (path + "/") in excluded_paths:
            # print('path + / is in excluded paths')
            return False
        elif path not in excluded_paths:
            # print('path not in excluded paths')
            return True

    def authorization_header(self,
                             request=None) -> str:
        '''Please i really REALLY hope this works'''
        if (request is not None and
           request.headers.get('Authorization')
           is not None):
            # print(request.headers.get('Authorization'))
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''For the current User in control'''
        return None

    def session_cookie(self, request=None):
        '''This is the session cookies request'''
        if not request:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        # print(cookie_name)
        cookie_value = request.cookies.get(cookie_name)
        return cookie_value
