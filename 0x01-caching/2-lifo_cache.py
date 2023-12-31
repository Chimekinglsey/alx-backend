#!/usr/bin/python3
"""
2. LIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching as Base


class LIFOCache(Base):
    """A caching system that removes items from cache Last-In-First-Out """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """sets new key and item to cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard_key = self.cache_data.popitem(last=True)
                print(f"DISCARD: {discard_key[0]}")

            self.cache_data[key] = item

    def get(self, key):
        """ retrieves a key if present in cache """
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data[key]
