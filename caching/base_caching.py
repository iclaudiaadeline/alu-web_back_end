#!/usr/bin/env python3
"""BaseCaching module
"""

class BaseCaching():
    """BaseCaching defines constants and storage for cache systems."""
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache storage."""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache contents sorted by key."""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache.

        Must be implemented by subclasses.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key.

        Must be implemented by subclasses.
        """
        raise NotImplementedError("get must be implemented in your cache class")
