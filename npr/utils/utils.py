'''
Utils for npr project
'''
from stuff.npr.settings import Settings
from pymongo import MongoClient


def get_db_client(db_name=''):
    '''
    :param db_name:
    :return:
    '''
    # http://api.mongodb.org/python/current/faq.html#multiprocessing
    c = MongoClient()
    return c

