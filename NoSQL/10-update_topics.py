#!/usr/bin/env python3
"""Python function that changes all topics of a school document based on the name"""


def updae_topics(mongo_collection, name, topics)


"""command that change all topics"""
mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
