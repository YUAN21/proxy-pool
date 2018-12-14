import time
from multiprocessing import Process

from DataBase import RedisClient
from VerifyProxy import VerifyProxys
from GetProxy import GetFreeProxy


class Schedule():
    @staticmethod
    def check_proxy():
        db = RedisClient()
        valid_proxy = VerifyProxys()
        get_proxies = GetFreeProxy()
        while True:
            print('检查代理池代理')
            pool_length = db.get_list_length()
            if pool_length < 10:
                print('代理数量严重不足，等待爬取ing')
            else:
                proxies = db.get_range_list(int(pool_length / 3))
                valid_proxy.verifyGroupProxys(proxies)
            time.sleep(10)

    @staticmethod
    def valid_pool():
        db = RedisClient()
        valid_proxy = VerifyProxys()
        get_proxies = GetFreeProxy()
        while True:
            print('检查代理池数量')
            pool_length = db.get_list_length()
            print('当前代理池数量：' + str(pool_length))
            if pool_length < 100:
                for get_proxy_function in get_proxies.functions:
                    proxys = get_proxy_function(get_proxies)
                    valid_proxy.verifyGroupProxys(proxys)
            time.sleep(10)

    def run(self):
        check_process = Process(target=Schedule.check_proxy)
        valid_process = Process(target=Schedule.valid_pool)
        valid_process.start()
        check_process.start()


def main():
    s = Schedule()
    s.run()


if __name__ == '__main__':
    main()
