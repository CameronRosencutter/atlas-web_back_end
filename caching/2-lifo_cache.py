#!/usr/bin/env python3


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This is the class of LIFOCache for cache"""
    def __init__(self):
        """This si the init function that will run at the end"""
        super().__init__()

    def put(self, key, item):
        """This si the put function that will run at the end"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """This si the get function that will run at the end"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
