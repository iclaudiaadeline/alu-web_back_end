#!/usr/bin/env python3
"""FIFOCache module

Implements a cache that discards the oldest item when full (FIFO).
"""

from collections import OrderedDict

try:
    from base_caching import BaseCaching
except ImportError:
    from caching.base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Cache using FIFO replacement policy."""

    def __init__(self):
        """Initialize FIFO cache with ordered storage."""
        super().__init__()
        self._order = OrderedDict()

    def put(self, key, item):
        """Add item to cache; discard oldest when exceeding MAX_ITEMS."""
        if key is None or item is None:
            return
        if key not in self._order:
            self._order[key] = None
        self.cache_data[key] = item
        # If over capacity, discard first inserted key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # pop first key from order
            oldest = next(iter(self._order))
            # remove from both structures
            self._order.pop(oldest, None)
            self.cache_data.pop(oldest, None)
            print("DISCARD: {}".format(oldest))

    def get(self, key):
        """Return value for key or None if not present."""
        if key is None:
            return None
        return self.cache_data.get(key)
