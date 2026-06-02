#!/usr/bin/env python3

"""
    a function that returns a tuple
    containing the start and end index for pagination.
"""


def index_range(page, page_size):
    """
    Return a tuple containing the start and end index for pagination.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)