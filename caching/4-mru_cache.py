#!/usr/bin/python3
"""MRU caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU cache implementation"""

    def __init__(self):
        """ Initialize MRU cache """
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # Update used_order
        if key in self.cache_data:
            self.used_order.remove(key)
        self.used_order.append(key)

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Remove the most recently used item (MRU)
            if self.used_order:
                mru_key = self.used_order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache """
        if key is None or key not in self.cache_data:
            return None

        # Update used_order
        self.used_order.remove(key)
        self.used_order.append(key)

        return self.cache_data[key]


if __name__ == "__main__":
    MRUCache = __import__('4-mru_cache').MRUCache

    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
