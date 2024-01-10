#!/usr/bin/env python3

"""importing the base_caching file needed"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """using the LRUcache chaching here"""
    def __init__(self):
        """This is the init function needed in the code"""
        super().__init__()

    def put(self, key, item):
        """This is the put function needed in the code"""
        if key is None or item is None:
            return

        # If cache is full, discard the least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """This is the get function needed in the code"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
