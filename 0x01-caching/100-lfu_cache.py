#!/usr/bin/python3
""" LFU Cache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.keys_usage = {}
        self.usage_keys = {}
        self.counter = 0
        self.min_usage = 1  # Initialize min_usage

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                while self.min_usage not in self.usage_keys or\
                        not self.usage_keys[self.min_usage]:
                    self.min_usage += 1

                min_usage_keys = self.usage_keys[self.min_usage]
                lru_key = min(min_usage_keys, key=lambda k: min_usage_keys[k])
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.keys_usage[lru_key]
                del self.usage_keys[self.min_usage][lru_key]

            self.cache_data[key] = item
            self.keys_usage[key] = 1
            self.usage_keys.setdefault(1, {})[key] = self.counter
            self.counter += 1
            self.min_usage = 1  # Reset min_usage after adding a new item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.keys_usage[key] += 1
            usage = self.keys_usage[key]
            old_usage = usage - 1
            del self.usage_keys[old_usage][key]
            if old_usage not in self.usage_keys:
                self.min_usage = old_usage + 1
            self.usage_keys.setdefault(usage, {})[key] = self.counter
            self.counter += 1
            return self.cache_data[key]
        return None
