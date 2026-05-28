#!/usr/bin/env python3
"""Core API v1 routes and error-triggering endpoints."""

from flask import abort, jsonify

from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """Return the API status payload."""

    return jsonify({"status": "OK"})


@app_views.route("/unauthorized", strict_slashes=False)
def unauthorized():
    """Trigger the unauthorized error handler."""

    abort(401)


@app_views.route("/forbidden", strict_slashes=False)
def forbidden():
    """Trigger the forbidden error handler."""

    abort(403)
