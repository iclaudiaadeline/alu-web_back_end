#!/usr/bin/env python3
"""User listing route for the API."""

from flask import jsonify

from api.v1.views import app_views
from models.user import User


@app_views.route("/users", strict_slashes=False)
def users():
    """Return all registered users as JSON."""

    return jsonify([user.to_dict() for user in User.search()])
