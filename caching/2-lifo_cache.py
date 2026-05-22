#!/usr/bin/env python3
"""LIFOCache module

Implements a cache that discards the most recently added/updated item when full (LIFO).
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Cache using LIFO replacement policy."""

    def __init__(self):
        """Initialize LIFO cache with ordered storage."""
        super().__init__()
        self._order = OrderedDict()

    def put(self, key, item):
        """Add or update item; if over capacity discard the last inserted/updated."""
        if key is None or item is None:
            return
        # If key exists, update and mark as most recent
        if key in self._order:
            # move to end to mark most recent
            self._order.pop(key, None)
        self._order[key] = None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # discard last inserted/updated
            last = next(reversed(self._order))
            self._order.pop(last, None)
            self.cache_data.pop(last, None)
            print("DISCARD: {}".format(last))

    def get(self, key):
        """Return value for key or None if not present."""
        if key is None:
            return None
        return self.cache_data.get(key)
