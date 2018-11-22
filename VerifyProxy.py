import aiohttp
import asyncio


class VerifyProxys():
    def __init__(self):
        pass

    async def verifySingleProxy(self, proxy):
        str_proxy = str(proxy)
        print('验证代理: ' + str_proxy)
        if not proxy[0] or not proxy[1]:
            return print('代理' + str_proxy + '似乎缺少必要数据')
        # DO 验证是否重复于数据库
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    proxy_url = 'http://' + proxy[0] + ':' + proxy[1]
                    async with session.get('http://www.baidu.com', proxy=proxy_url, timeout=30) as response:
                        if response.status == 200:
                            print('这是一个好代理：'+str_proxy+'')  
                            # DO 入库
                except Exception as e:
                    print('错误代理：' + str_proxy + str(e))
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
