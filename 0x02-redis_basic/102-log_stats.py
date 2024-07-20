#!/usr/bin/env python3
"""
102-log_stats
"""


if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(nginx.count_documents({}), 'logs')

    print('Methods:')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for meth in methods:
        counted = nginx.count_documents({'method': meth})
        print('\tmethod {}: {}'.format(meth, counted))

    status_check_count = nginx.count_documents({'method': 'GET',
                                                'path': '/status'})
    print('{} status check'.format(status_check_count))

    print('IPs:')
    pipeline = [
        {'$group':
            {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
         },
        {'$sort':
            {'count': -1}
         },
        {'$limit': 10}
    ]
    ip_count = nginx.aggregate(pipeline)

    for ip in ip_count:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')
