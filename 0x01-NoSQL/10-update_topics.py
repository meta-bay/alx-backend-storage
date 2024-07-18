#!/usr/bin/env python3
'''
    10-update_topics
'''


def update_topics(mongo_collection, name, topics):
    '''change school topics'''
    mongo_collection.update_one(name, str(topics))

if __name__ == "__main__":
    update_topics(mongo_collection, name, topics)

