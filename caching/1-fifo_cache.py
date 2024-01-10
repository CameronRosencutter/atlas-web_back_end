#!/usr/bin/env python3

"""2 problem"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache"""

    def __init__(self):
        """ Initialize FIFOCache instance with parent init  """
        super().__init__()

    def put(self, key, item):
        """ Add"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """gt """
        return self.cache_data.get(key, None)
    