#!/usr/bin/env python3
""" function floor which returns the floor of the float.
"""


def floor(n: float) -> int:
    """ Return the floor of float """
    return int(n) if n >= 0 else int(n) - 1
