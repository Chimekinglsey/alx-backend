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

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                keys_to_discard = []
                min_usage = min(self.keys_usage.values())
                for k, v in self.keys_usage.items():
                    if v == min_usage:
                        keys_to_discard.append(k)
                if len(keys_to_discard) > 1:
                    lru_key = min(self.usage_keys[min_usage], key=lambda x:
                                  self.usage_keys[min_usage][x])
                    keys_to_discard.remove(lru_key)
                for k in keys_to_discard:
                    del self.cache_data[k]
                    del self.keys_usage[k]
                    del self.usage_keys[min_usage][k]
                    print(f"DISCARD: {k}")
            self.cache_data[key] = item
            if key in self.keys_usage:
                self.keys_usage[key] += 1
            else:
                self.keys_usage[key] = 1
            if 1 not in self.usage_keys:
                self.usage_keys[1] = {}
            self.usage_keys[1][key] = self.counter
            self.counter += 1

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.keys_usage[key] += 1
            usage = self.keys_usage[key]
            del self.usage_keys[usage - 1][key]
            if usage not in self.usage_keys:
                self.usage_keys[usage] = {}
            self.usage_keys[usage][key] = self.counter
            self.counter += 1
            return self.cache_data[key]
        return None
