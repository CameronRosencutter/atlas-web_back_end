#!/usr/bin/env python3

"""importing the base_caching file needed"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache Implementation

    This class inherits from the BaseCaching class
    """
    def __init__(self):
        """Initialize an empty MRU cache."""
        super().__init__()

    def put(self, key, item):
        """This is the put function needed in the code"""
        if key is None or item is None:
            return

        # Check if the cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the most recently used key
            mru_key = next(iter(self.cache_data))

            # Discard the most recently used item
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Assign the item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """This is the get function needed in the code"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
