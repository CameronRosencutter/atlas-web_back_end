#!/usr/bin/env python3

""" first problem """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Cache"""

    def put(self, key, item):
        """put"""
        if key is not None and item is not None:
            self.cache_data[key] = item