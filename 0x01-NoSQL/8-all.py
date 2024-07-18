#!/usr/bin/env python3
'''
    8-all.py
'''


def list_all(mongo_collection):
    ''' Return an empty list if no document in the collection '''
    return mongo_collection.find()

if __name__ == "__main__":
    list_all(mongo_collection)

