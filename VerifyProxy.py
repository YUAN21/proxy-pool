import aiohttp
import asyncio
from DataBase import RedisClient


class VerifyProxys():
    def __init__(self):
        self.db = RedisClient()

    async def verifySingleProxy(self, proxy):
        # DO 验证是否重复于数据库
        print('当前代理：' + proxy)
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    proxy_url = 'http://' + proxy
                    async with session.get('http://www.baidu.com', proxy=proxy_url, timeout=30) as response:
                        if response.status == 200:
                            print('可用代理：' + proxy + '，准备入库')
                            self.db.storage(proxy)

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
            print('多代理数据验证错误【GROUP】' + str(groupProxyMsgs))
            print(e)
