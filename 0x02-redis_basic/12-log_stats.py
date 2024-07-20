#!/usr/bin/env python3
"""
12-log_stats
"""
if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(nginx.count_documents({}), 'logs')
    print('Methods:')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for meth in methods:
        coutned = nginx.count_documents({'method': meth})
        print('\tmethod {}: {}'.format(meth, coutned))

    count_stat = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print('{} status check'.format(count_stat))
