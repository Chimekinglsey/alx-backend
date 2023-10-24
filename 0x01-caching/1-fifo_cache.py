#!/usr/bin/python3
"""
1. FIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching as Base


class FIFOCache(Base):
    """A caching system that removes items from cache First-In-First-Out """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """sets new key and item to cache """
        if key is None or item is None:
            pass
        elif len(self.cache_data) <= Base.MAX_ITEMS:
            self.cache_data[key] = item

        else:
            discard = self.cache_data.popitem(last=False)[0]
            print(f"DISCARD: {discard}")
            self.cache_data[key] = item

    def get(self, key):
        """ retrieves a key if present in cache """
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data[key]
