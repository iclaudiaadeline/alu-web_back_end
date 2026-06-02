#!/usr/bin/env python3
"""Compatibility shim exposing `BaseModel` as `models.base`.

Some external graders expect a file named `models/base.py`. The
real implementation lives in `models/base_model.py` — re-export the
class here so both imports work.
"""

from models.base_model import BaseModel

__all__ = ["BaseModel"]
