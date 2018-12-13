import asyncio
import random

import aiohttp

from DataBase import RedisClient


class VerifyProxys():
    def __init__(self):
        self.db = RedisClient()

    async def verifySingleProxy(self, proxy):
        print('当前验证代理：' + proxy)
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    proxy_url = 'http://' + proxy
                    # async with session.get('http://www.baidu.com', proxy=proxy_url, timeout=30) as response:
                    async with session.get('http://www.baidu.com', timeout=30) as response:
                        if response.status == 200:
                            if random.randint(1, 10) <=7:
                                print('可用代理：' + proxy + '，准备入库')
                                self.db.remove_duplicate_values(proxy)
                                self.db.storage(proxy)
                            else:
                                print('伪代理池随机抛弃代理：' + proxy)
                except Exception as e:
                    print('不可用代理：' + proxy + ',' + str(e))
        except:
            pass

    def verifyGroupProxys(self, groupProxyMsgs):
        print('开始验证多个代理数据【GROUP】')
        try:
            loop = asyncio.get_event_loop()
            tasks = [self.verifySingleProxy(proxyMsg)
                     for proxyMsg in groupProxyMsgs]
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as e:
            print('多代理数据验证错误【GROUP】')
            print(e)
