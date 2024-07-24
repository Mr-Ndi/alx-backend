#!/usr/bin/env python3
"""
A module that contains a class FIFOCache that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implementation of a FIFO caching system from BaseCaching
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.keys = []  # List to maintain the order of keys

    def put(self, key, item):
        """
        Add an element to the cache using FIFO strategy.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        self.cache_data[key] = item
        self.keys.append(key)  # Add the key to the end of the list

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first key added (FIFO)
            first_key = self.keys.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found
        else:
            return self.cache_data[key]
