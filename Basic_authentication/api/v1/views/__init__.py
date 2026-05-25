#!/usr/bin/env python3
"""Blueprint registration for API v1 views."""

from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views import index  # noqa: E402,F401
from api.v1.views import users  # noqa: E402,F401
