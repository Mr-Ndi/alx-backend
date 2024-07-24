#!/usr/bin/env python3
"""
A module that contains a class LFUCache that inherits
from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Implementation of an LFU caching system from BaseCaching
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = {}  # Dictionary to keep track of frequency of keys
        self.usage = {}  # Dictionary to keep track of the order of keys for LFU
        self.min_freq = 0  # Track the minimum frequency

    def put(self, key, item):
        """
        Add an element to the cache using LFU strategy.
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        if key in self.cache_data:
            # Update the existing item
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        # Add new item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict()

        self.cache_data[key] = item
        self.frequency[key] = 1
        if 1 not in self.usage:
            self.usage[1] = []
        self.usage[1].append(key)
        self.min_freq = 1

    def get(self, key):
        """
        Retrieve an element from the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found

        self._update_frequency(key)
        return self.cache_data[key]  # Return the value associated with the key

    def _update_frequency(self, key):
        """Update the frequency of a key."""
        freq = self.frequency[key]
        self.frequency[key] += 1

        # Move the key to the next frequency list
        self.usage[freq].remove(key)
        if not self.usage[freq]:
            del self.usage[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        new_freq = freq + 1
        if new_freq not in self.usage:
            self.usage[new_freq] = []
        self.usage[new_freq].append(key)

    def _evict(self):
        """Evict the least frequently used item."""
        lfu_keys = self.usage[self.min_freq]
        lfu_key = lfu_keys.pop(0)  # Get the least recently used key among those with min frequency
        if not lfu_keys:
            del self.usage[self.min_freq]

        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        print(f"DISCARD: {lfu_key}")

        if self.usage:
            self.min_freq = min(self.usage.keys())
        else:
            self.min_freq = 0
