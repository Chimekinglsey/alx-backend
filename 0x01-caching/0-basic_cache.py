#!/usr/bin/python3
"""
0-basic_cache.py
"""
from base_caching import BaseCaching as Base


class BasicCache(Base):
    """A basic caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns key and item to the parent class self.cache_data """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves the value of a key from self.cache_data if it exists"""
        if key is None or not self.cache_data.get(key):
            return None
        else:
            return self.cache_data.get(key)
