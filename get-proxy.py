from fake_useragent import UserAgent
import requests
import time
import re
ua = UserAgent()


def getPage(url):
    headers = {
        'User-Agent':  ua.random,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return False
    except:
        return False


class GetFreeProxy():
    def fromKuaiDaiLi(self):
        print('开始从【快代理】获取数据')
        KdlRe = re.compile('<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\d+)</td>')
        try:
            for page in range(1, 2):
                url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
                html = getPage(url)
                if html:
                    proxyMsg = KdlRe.findall(html)
                    print(proxyMsg)
                    for msg in proxyMsg:
                        print(msg[0])
                    time.sleep(3)
        except:
            print('从【快代理】获取数据失败')

    def fromXiCi(self):
        print('开始从【西刺代理】获取数据')
        XcRe = re.compile('<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
        try:
            for page in range(1, 2):
                url = 'http://www.xicidaili.com/nn/{}'.format(page)
                html = getPage(url)
                print(html)
                if html:
                    proxyMsg = XcRe.findall(html)
                    for msg in proxyMsg:
                        print(msg)
                    time.sleep(3)
        except:
            print('从【西刺代理】获取数据失败')

    def from5U(self):
        print('开始从【无忧代理】获取数据')
        WuYouRe = re.compile('<ul class="l2">\s*<span>\s*<li>(.*)</li>\s*</span>\s*<span style=".*">\s*<li class=".*">(\d+)</li>\s*</span>')
        try:
            url = 'http://www.data5u.com/'
            html = getPage(url)
            if html:
                proxyMsg = WuYouRe.findall(html)
                print(proxyMsg)
                for msg in proxyMsg:
                    print(msg)
        except:
            print('从【无忧代理】获取数据失败')


        
def main():
    g = GetFreeProxy()
    g.from5U()


if __name__ == '__main__':
    main()
