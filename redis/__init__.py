# TODO 没有coding声明的原因？
from redis.client import Redis, StrictRedis

# TODO import多个包时的写法是采用tuple，而不是多行拼接。
from redis.connection import (
    BlockingConnectionPool,
    ConnectionPool,
    Connection,
    SSLConnection,
    UnixDomainSocketConnection
)
from redis.utils import from_url
from redis.exceptions import (
    AuthenticationError,
    BusyLoadingError,
    ConnectionError,
    DataError,
    InvalidResponse,
    PubSubError,
    ReadOnlyError,
    RedisError,
    ResponseError,
    TimeoutError,
    WatchError
)

# TODO 该方法是否会在from redis import * 时被导入呢？
def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


__version__ = '3.2.1'
VERSION = tuple(map(int_or_str, __version__.split('.')))  # TODO 使用map代替for中的单行函数调用写法。

# TODO 控制from redis import *的导入结果。
__all__ = [
    'Redis', 'StrictRedis', 'ConnectionPool', 'BlockingConnectionPool',
    'Connection', 'SSLConnection', 'UnixDomainSocketConnection', 'from_url',
    'AuthenticationError', 'BusyLoadingError', 'ConnectionError', 'DataError',
    'InvalidResponse', 'PubSubError', 'ReadOnlyError', 'RedisError',
    'ResponseError', 'TimeoutError', 'WatchError'
]
