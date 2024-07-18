#!/usr/bin/env python3
'''
    9-insert_school
'''


def insert_school(mongo_collection, **kwargs):
    ''' Returns the new _id '''
    return mongo_collection.insert_one(kwargs).inserted_id

if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)

