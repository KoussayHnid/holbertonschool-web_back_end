#!/usr/bin/env python3
''' Basic authentication '''
from flask import request


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True

def authorization_header(self, request=None) -> str:
    if request is None:
            return None

def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return


