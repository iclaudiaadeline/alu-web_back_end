#!/usr/bin/env python3
"""Basic Authentication implementation for API v1."""

import base64
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication helper methods."""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Return the Base64 part of a Basic Authorization header."""

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a Base64 authorization payload into UTF-8 text."""

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Split decoded credentials into user email and password."""

        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar("User"):
        """Return a User instance that matches the provided credentials."""

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search(email=user_email)
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar("User"):
        """Return the authenticated user from a request."""

        authorization = self.authorization_header(request)
        if authorization is None:
            return None

        base64_authorization = self.extract_base64_authorization_header(
            authorization)
        if base64_authorization is None:
            return None

        decoded = self.decode_base64_authorization_header(
            base64_authorization)
        if decoded is None:
            return None

        email, password = self.extract_user_credentials(decoded)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
