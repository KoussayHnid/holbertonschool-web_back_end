#!/usr/bin/python3
""" FIFOCache module"""

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initialize FIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using FIFO algorithm"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]

if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
