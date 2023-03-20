from urllib import parse
from redis import ConnectionPool, StrictRedis


def get_client():
    url = "redis://127.0.0.1:6379"
    parse_url = parse.urlparse(url)
    cache_params = {
                "host": parse_url.hostname,
                "port": parse_url.port,
                "db": parse_url.path.replace("/", ""),
                "password": parse_url.password,
                "username": parse_url.username,
            }
    redis_pool = ConnectionPool(**cache_params)
    client = StrictRedis(connection_pool=redis_pool)
    return client