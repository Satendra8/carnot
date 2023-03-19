from urllib import parse
from redis import ConnectionPool, StrictRedis


def get_client():
    url = "redis-19999.c245.us-east-1-3.ec2.cloud.redislabs.com:19999"
    parse_url = parse.urlparse(url)
    cache_params = {
                "host": "redis-19999.c245.us-east-1-3.ec2.cloud.redislabs.com",
                "port": 19999,
                "password": "RE3qQrhqiIgiy380aA82ZQFcDpvDJlyN",
            }
    redis_pool = ConnectionPool(**cache_params)
    client = StrictRedis(connection_pool=redis_pool)
    return client