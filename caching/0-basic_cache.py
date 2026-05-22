#!/usr/bin/env python3
"""BasicCache module

This module implements a simple caching system with no size limit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache implementation with unlimited size."""

    def put(self, key, item):
        """Assign the item to `key` in the cache.

        Do nothing if key or item is None.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to `key` or None if not found."""
        if key is None:
            return None
        return self.cache_data.get(key)
