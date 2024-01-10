#!/usr/bin/env python3

"""This is importing base_caching from the current repo. """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Im not super sure what to say here. Im barely understanding this."""

    def put(self, key, item):
        """Here are more words to see if this is whats counting."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve a value from the cache."""
        return self.cache_data.get(key, None)
