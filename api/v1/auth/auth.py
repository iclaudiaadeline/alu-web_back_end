#!/usr/bin/env python3
"""Base authentication template for API v1."""

from typing import List, TypeVar

from flask import request


class Auth:
    """Base class for all authentication systems."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return whether the given path requires authentication."""

        if path is None:
            return True
        if not excluded_paths:
            return True

        def normalize(value: str) -> str:
            """Normalize a path for slash-tolerant comparison."""

            if value == "/":
                return "/"
            return value.rstrip("/")

        normalized_path = normalize(path)
        for excluded_path in excluded_paths:
            if normalize(excluded_path) == normalized_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header value from a request."""

        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """Return the current user for a request."""

        return None
