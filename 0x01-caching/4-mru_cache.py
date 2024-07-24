#!/usr/bin/env python3
"""
A module that contains a class MRUCache that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Implementation of an MRU caching system from BaseCaching
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []  # List to track the order of keys for MRU

    def put(self, key, item):
        """
        Add an element to the cache using MRU strategy.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If the key already exists, update its value and mark it as recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)  # Remove the key from its current position
        else:
            self.cache_data[key] = item

        self.order.append(key)  # Add the key to the end of the order list

        # Check if we exceed the maximum number of items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = self.order.pop(-2)  # Get the second to last key added (most recently used)
            del self.cache_data[mru_key]  # Remove it from cache
            print(f"DISCARD: {mru_key}")  # Print the discarded key

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found

        if key in self.order:
            self.order.remove(key)  # Remove the key from its current position
            self.order.append(key)  # Append it to the end to mark it as recently used

        return self.cache_data[key]  # Return the value associated with the key
