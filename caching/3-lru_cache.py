#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """ Initialize LRUCache instance.
        """
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm.
        """
        if key is None or item is None:
            return

        # Update used_order
        if key in self.cache_data:
            self.used_order.remove(key)
        self.used_order.append(key)

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Remove the least recently used item (LRU)
            lru_key = self.used_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update used_order
        self.used_order.remove(key)
        self.used_order.append(key)

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LRUCache()
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
