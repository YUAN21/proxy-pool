
class VerifyProxys():
    def __init__(self):
        pass

    async def verifySingleProxy(self, proxy):
        print('验证代理: ' + proxy)
        '''
        DO 验证是否重复
        '''
        proxy_url = 'http://' + proxy

    def verifyGroupProxys(self, groupProxyMsgs):
        for proxyMsg in groupProxyMsgs:
            if isinstance(proxyMsg, tuple) and proxyMsg[0] and proxyMsg[1]:
                proxyMsg = proxyMsg[0] + ':' + proxyMsg[1]
            self.verifySingleProxy(proxyMsg)