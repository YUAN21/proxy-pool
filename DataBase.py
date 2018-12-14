import redis


class RedisClient():
    def __init__(self):
        self.dbClient = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def storage(self, proxy):
        self.dbClient.rpush('proxies', proxy)
        
    def get_list_length(self):
        return self.dbClient.llen('proxies')

    def get_range_list(self, count):
        proxies = self.dbClient.lrange('proxies', 0, count - 1)
        self.dbClient.ltrim('proxies', count - 1, -1)
        return proxies

    def remove_duplicate_values(self, value):
        self.dbClient.lrem('proxies', 0, value)

    def get_proxy(self):
        return self.dbClient.rpop('proxies')