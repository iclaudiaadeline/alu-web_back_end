#!/usr/bin/env python3
"""LRUCache module

Implements a cache that discards the least recently used item when full (LRU).
"""

from collections import OrderedDict

try:
    from base_caching import BaseCaching
except ImportError:
    from caching.base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Cache using LRU replacement policy."""

    def __init__(self):
        """Initialize LRU cache with ordered storage tracking usage."""
        super().__init__()
        self._order = OrderedDict()

    def put(self, key, item):
        """Add or update item; discard least recently used when full."""
        if key is None or item is None:
            return
        if key in self._order:
            # update usage: move to end as most recently used
            self._order.pop(key, None)
        self._order[key] = None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # remove least recently used (first)
            lru = next(iter(self._order))
            self._order.pop(lru, None)
            self.cache_data.pop(lru, None)
            print("DISCARD: {}".format(lru))

    def get(self, key):
        """Return value for key and update its recentness."""
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        # mark as recently used
        self._order.pop(key, None)
        self._order[key] = None
        return self.cache_data.get(key)
