#!/usr/bin/env python3

"""
    A basic caching algorithm.

    Attributes:
        capacity (int): Maximum number of items the cache can hold.
        cache (dict): Dictionary to store key-value pairs.
    """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
        """
    A basic caching algorithm.

    Attributes:
        capacity (int): Maximum number of items the cache can hold.
        cache (dict): Dictionary to store key-value pairs.
    """

    def put(self, key, item):
        """put"""
        if key is not None and item is not None:
            self.cache_data[key] = item