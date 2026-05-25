#!/usr/bin/env python3
"""User model used by the authentication project."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent an API user stored in the file-based storage."""

    def __init__(self, *args, **kwargs):
        """Create a user instance or restore it from storage."""

        self.email = ""
        self.password = ""
        self.first_name = None
        self.last_name = None
        super().__init__(*args, **kwargs)

    def display_name(self):
        """Return the user's display name."""

        parts = [self.first_name, self.last_name]
        return " ".join(part for part in parts if part)

    def is_valid_password(self, password):
        """Return whether the provided password matches the user."""

        return self.password == password

    @classmethod
    def search(cls, **kwargs):
        """Search for users in storage using the provided filters."""

        from models.engine.file_storage import storage

        return storage.search(cls, **kwargs)
