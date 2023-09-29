#!/usr/bin/env python3
"""scripte that change school topics"""


def updae_topics(mongo_collection, name, topics)


""" that how to change all topics"""
return mongo_collection.update_many(
    {"name": name}, {"$set": {"topics": topics}})
