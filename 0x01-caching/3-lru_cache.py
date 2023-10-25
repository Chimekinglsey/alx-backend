#!/usr/bin/python3
"""
3. Least Recently Used Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system that removes Least Recently Used items from cache"""
    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_log = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_log[key] += 1
                self.cache_data.move_to_end(key)
            else:
                self.access_log[key] = 0
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lru_key, lru_val = self.cache_data.popitem(last=False)
                    self.access_log.pop(lru_key)
                    print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache by key"""
        if key is not None and key in self.cache_data:
            self.access_log[key] += 1
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
