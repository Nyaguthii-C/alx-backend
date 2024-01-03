#!/usr/bin/env python3
"""Caching: basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherit from BaseCaching and is a caching system"""
    def put(self, key, item):
        """assign item value to key in cache dictionary"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in cache dictionary linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
