#!/usr/bin/env python3
"""insert a new doc in collection """


def insert_school(mongo_collection, **kwargs)

"""insert a new doc"""
return mongo_collection.insert_one(kwargs).inserted_id
