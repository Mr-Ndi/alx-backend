#!/usr/bin/env python3
"""
A module that contains a Create a class BasicCache that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implementation of a caching system from BaseCaching
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """
        Add an element to the cache.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None
        else:
            # Store the item in the cache
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found
        else:
            return self.cache_data[key]
