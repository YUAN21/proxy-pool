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
        response = requests.get(url, headers = headers, timeout = 3)
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
        for page in range(1, 2):
            url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
            html = getPage(url)
            if html:
                proxyMsg = KdlRe.findall(html)
                print(proxyMsg)
                for s in proxyMsg:
                    print(s[0])
                time.sleep(3)

def main():
    g = GetFreeProxy()
    g.fromKuaiDaiLi()


if __name__ == '__main__':
    main()
