import time

from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.cassandra.ttypes import NotFoundException

__all__ = ['get_user_by_userid', 'DatabaseError',
    'NotFound', 'InvalidDictionary']

POOL = ConnectionPool(keyspace='TEST', server_list=['localhost:9160'], prefill=False)

USER = ColumnFamily(POOL, 'Users')
Board = ColumnFamily(POOL, 'Board')

class DatabaseError(Exception):
    """
    The base error that functions in this module will raise when things go
    wrong.
    """
    pass

class NotFound(DatabaseError):
    pass


class InvalidDictionary(DatabaseError):
    pass

def get_user_by_userid(userid):
    try:
        user = USER.get(str(userid), columns=['name', 'password'])
    except NotFoundException:
        raise NotFound('User %s not found' % (userid,))
    return user

def get_user_by_userid(userid):
    try:
        user = USER.get(str(userid), columns=['name', 'password'])
    except NotFoundException:
        raise NotFound('User %s not found' % (userid,))
    return user

def get_thread_by_threadid(threadid):
    try:
        board = Board.get(str(threadid, columns=['res'])
    except NotFoundException:
        raise NotFound('Thread %s not found' % (threadid,))
    return thread



