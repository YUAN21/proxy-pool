import redis

class RedisClient():
    def __init__(self):
        self.dbClient = redis.Redis(host='localhost', port=6379)

    def storage(self, proxy):
        self.dbClient.rpush('proxies', proxy)
