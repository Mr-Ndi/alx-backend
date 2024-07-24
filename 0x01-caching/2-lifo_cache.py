#!/usr/bin/env python3
"""
A module that contains a class LIFOCache that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implementation of a LIFO caching system from BaseCaching
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.keys = []  # List to maintain the order of keys

    def put(self, key, item):
        """
        Add an element to the cache using LIFO strategy.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If the key already exists, update its value and mark it
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update the order by removing the old key and adding it back
            self.keys.remove(key)  # Remove the old key
        else:
            # Add new key-value pair to the cache
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last key added (LIFO)
                last_key = self.keys.pop()  # Get the last key added
                del self.cache_data[last_key]  # Remove it from cache
                print(f"DISCARD: {last_key}")  # Print the discarded key

        self.cache_data[key] = item
        self.keys.append(key)  # Track the order of keys

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found
        return self.cache_data[key]  # Return the value associated with the key
