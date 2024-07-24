#!/usr/bin/env python3
"""
A module that contains a class LRUCache that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implementation of an LRU caching system from BaseCaching
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []  # List to track the order of keys for LRU

    def put(self, key, item):
        """
        Add an element to the cache using LRU strategy.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If the key already exists, update its value and mark it as recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)  # Remove the key from its current position
        else:
            self.cache_data[key] = item
            # Check if we exceed the maximum number of items
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the least recently used item
                lru_key = self.order.pop(0)  # Get the first key (least recently used)
                del self.cache_data[lru_key]  # Remove it from cache
                print(f"DISCARD: {lru_key}")  # Print the discarded key

        self.order.append(key)  # Add the key to the end to mark it as recently used

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found

        # Mark the key as recently used by moving it to the end of the order list
        self.order.remove(key)  # Remove the key from its current position
        self.order.append(key)  # Append it to the end to mark it as recently used
        return self.cache_data[key]  # Return the value associated with the key
