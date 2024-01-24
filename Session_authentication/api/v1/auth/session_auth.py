#!/usr/bin/env python3
'''
This is the session_auth.py file
'''
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
import os
import uuid
import base64


class SessionAuth(Auth):
    '''For the class session and author'''

    user_id_by_session_id: dict = {}

    def __init__(self) -> None:
        '''This is the init file'''
        super().__init__()

    def create_session(self,
                       user_id: str = None
                       ) -> str:
        '''Create a session for the user'''
        if (not user_id or
           not isinstance(user_id, str)):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self,
                               session_id: str = None
                               ) -> str:
        '''Find the id for the session'''
        if (not session_id or
           not isinstance(session_id, str)):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        '''Determinies who is the current user'''
        session_cookie = str(self.session_cookie(request))
        # print('session cookie is:', session_cookie)
        current_user = self.user_id_for_session_id(session_cookie)
        # print('current user is:', current_user)

        user_cls = User()
        user = user_cls.get(current_user)
        # print('user is:', user)

        return user

    def destroy_session(self, request=None):
        '''Terminates the session witht he current user'''
        cookie_value = self.session_cookie(request)
        if (not request or
           not cookie_value):
            return False

        user_id = self.user_id_for_session_id(cookie_value)
        if not user_id:
            return False

        del self.user_id_by_session_id[cookie_value]
        return True