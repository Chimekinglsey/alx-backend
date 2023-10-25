#!/usr/bin/python3
"""
3. Most Recently Used Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system that removes Most Recently Used items from cache"""
    def __init__(self):
        """Initialize the MRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_log = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_log[key] += 1
                self.cache_data.move_to_end(key, last=False)
            else:
                self.access_log[key] = 0
                if len(self.cache_data) >= self.MAX_ITEMS:
                    mru_key,mru_val = self.cache_data.popitem(last=False)
                    self.access_log.pop(mru_key)
                    print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache by key"""
        if key is not None and key in self.cache_data:
            self.access_log[key] += 1
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
