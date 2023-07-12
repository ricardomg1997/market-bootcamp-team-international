from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv



try: 
    redis_client = Redis(
        host='enough-wren-43010.upstash.io',
        port=43010,
        password='5550122d9d3340f5bf93f798c29132d4'
        )
    print("Connecte to redis")
except ConnectionError as e:
    print(e)
