#!/usr/bin/env python3
"""Caching: basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherit from BaseCaching and is a caching system"""
    def put(self, key, item):
        """assign item value to key in cache dictionary"""
        self.cache_data[key] = item
        if key or item is None:
            pass

    def get(self, key):
        """return the value in cache dictionary linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
