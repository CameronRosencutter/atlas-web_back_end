#!/usr/bin/env python3

"""This is importing base_caching from the current repo. """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Im not super sure what to say here. Im barely understanding this."""

    def put(self, key, item):
        """put"""
        if key is not None and item is not None:
            self.cache_data[key] = item