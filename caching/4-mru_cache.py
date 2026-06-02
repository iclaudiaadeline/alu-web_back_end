#!/usr/bin/env python3
"""MRUCache module

Implements a cache that discards the most recently used item when full (MRU).
"""

from collections import OrderedDict

try:
    from base_caching import BaseCaching
except ImportError:
    from caching.base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Cache using MRU replacement policy."""

    def __init__(self):
        """Initialize MRU cache with ordered storage tracking usage."""
        super().__init__()
        self._order = OrderedDict()

    def put(self, key, item):
        """Add or update item; discard most recently used when full."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self._order.pop(key, None)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = next(reversed(self._order))
            self._order.pop(mru, None)
            self.cache_data.pop(mru, None)
            print("DISCARD: {}".format(mru))
        self._order[key] = None
        self.cache_data[key] = item

    def get(self, key):
        """Return value for key and update its recentness."""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        # mark as most recently used
        self._order.pop(key, None)
        self._order[key] = None
        return self.cache_data.get(key)
