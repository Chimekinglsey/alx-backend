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
        if key is not None and item is not None:
            for k,v in self.cache_data.items():
                if key not in self.access_log.keys():
                    self.access_log[key] = [item, self.get_count]
            if len(self.cache_data) >= self.MAX_ITEMS:
                for k,v in self.access_log.items():
                    lru, rmv = min(0, v[1]), k
                if self.cache_data.get(rmv):
                    discard_key = self.cache_data.pop(rmv)
                    print(f"DISCARD: {discard_key}")
                else:
                    for k, v in self.cache_data.items():
                        if k is rmv:
                            continue
                        if v[1] == 0:
                            discard_key = self.cache_data.pop(k)
                            print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ retrieves a key if present in cache """
        if key is None or not self.cache_data.get(key):
            return None
        for k,v in self.cache_data.items():
            if key in self.cache_data and key in self.access_log and key == k:
                self.access_log[key][1] += 1
        return self.cache_data[key]
"""
from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_log = {}  # Store access counts for keys

    def put(self, key, item):
        if key is not None and item is not None:
            # Check if the key is already in the cache
            if key in self.cache_data:
                # Update the access count for the existing key
                self.access_log[key] += 1
                # Update the item in the cache
                self.cache_data.move_to_end(key)
            else:
                # Add the key with an access count of 0
                self.access_log[key] = 0
                # If the cache is full, remove the LRU item
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lru_key = next(iter(self.cache_data))
                    self.cache_data.pop(lru_key)
                    self.access_log.pop(lru_key)

            # Add the new key-value pair
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            # Update the access count for the accessed key
            self.access_log[key] += 1
            # Move the accessed key to the end to mark it as the most recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

"""