#!/usr/bin/env python3

"""importing the base_caching file needed"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache"""

    def __init__(self):
        """ Initialize FIFOCache instance with parent init  """
        super().__init__()

    def put(self, key, item):
        """ This is the add function that will operate at the end"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """This si the get function that will run at the end"""
        return self.cache_data.get(key, None)
