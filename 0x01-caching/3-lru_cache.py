#!/usr/bin/python3
"""
3. Least Recently Used Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching as Base


class LRUCache(Base):
    """A caching system that removes
        Least Recently Used items from cache
    """
    access_log = {}
    get_count = 0

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """sets new key and item to cache """
        for k,v in self.cache_data.items():
            if not self.access_log.get(k[1]):
                self.access_log[k] = [v, self.get_count]
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                for k,v in self.access_log.items():
                    lru = min(k[1])
                discard_key = self.cache_data.pop(lru)
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ retrieves a key if present in cache """
        if key is None or not self.cache_data.get(key):
            return None
        for k,v in self.cache_data.items():
            self.access_log[k] = [v, self.get_count]
            if key == k:
                self.access_log[k[1]] += 1
        return self.cache_data[key]
