#!/usr/bin/env python3
"""Caching:  FIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """inherit from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assign item value to key in cache dictionary
        Update the order of insertion into cache
        delete first item inserted in cache

        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = self.order.pop(0)
                del self.cache_data[first_item]
                print(f"DISCARD: {first_item}")

    def get(self, key):
        """return the value in cache dictionary linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
