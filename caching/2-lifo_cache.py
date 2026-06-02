#!/usr/bin/env python3
"""LIFOCache module

Implements a cache that discards the most recently added/updated item when full (LIFO).
"""

from collections import OrderedDict

try:
    from base_caching import BaseCaching
except ImportError:
    from caching.base_caching import BaseCaching


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
        if key in self.cache_data:
            self._order.pop(key, None)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = next(reversed(self._order))
            self._order.pop(last, None)
            self.cache_data.pop(last, None)
            print("DISCARD: {}".format(last))
        self._order[key] = None
        self.cache_data[key] = item

    def get(self, key):
        """Return value for key or None if not present."""
        if key is None:
            return None
        return self.cache_data.get(key)
