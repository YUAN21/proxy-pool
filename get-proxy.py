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


class ProxyMetaclass(type):
    """
        万物皆虚 万事皆允
        python中所有的量都是对象
        这里 ProxyMetaclass 定义的是元类  理解为类的类
        type() 可以用来创建类 参数：type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
        也就对应了  __new__(cls 实例本身 类似self 这里就是<class '__main__.ProxyMetaclass'>, name 类名 这里就是 GetFreeProxy, bases 父类 这里就是(), attrs 内容 参数 这里就是GetFreeProxy中默认的和定义了的function)  中的参数
    """
    def __new__(cls, name, bases, attrs):
        functions = []
        for function_name, function_content in attrs.items():
            # 筛选排除默认的 如__init__等函数
            if 'from' in function_name:
                functions.append(function_content)
        attrs['functions'] = functions
        # 元类必须返回一个类
        # 这就是基本的OOP编程。由于type是元类也就是类，因此它本身也是通过__new__方法生成其实例，只不过这个实例是一个类.
        return type.__new__(cls, name, bases, attrs)


class GetFreeProxy(metaclass=ProxyMetaclass):
    def fromKuaiDaiLi(self):
        print('开始从【快代理】获取数据')
        KdlRe = re.compile(
            '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\d+)</td>')
        try:
            proxys = []
            for page in range(1, 2):
                url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
                html = getPage(url)
                if html:
                    proxyMsg = KdlRe.findall(html)
                    for msg in proxyMsg:
                        proxys.append(msg)
                    time.sleep(3)
            return proxys
        except:
            print('从【快代理】获取数据失败')

    def fromXiCi(self):
        print('开始从【西刺代理】获取数据')
        XcRe = re.compile(
            '<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
        try:
            proxys = []
            for page in range(1, 2):
                url = 'http://www.xicidaili.com/nn/{}'.format(page)
                html = getPage(url)
                if html:
                    proxyMsg = XcRe.findall(html)
                    for msg in proxyMsg:
                        proxys.append(msg)
                    time.sleep(3)
            return proxys
        except:
            print('从【西刺代理】获取数据失败')

    def from5U(self):
        print('开始从【无忧代理】获取数据')
        WuYouRe = re.compile(
            '<ul class="l2">\s*<span>\s*<li>(.*)</li>\s*</span>\s*<span style=".*">\s*<li class=".*">(\d+)</li>\s*</span>')
        try:
            url = 'http://www.data5u.com/'
            html = getPage(url)
            if html:
                proxyMsg = WuYouRe.findall(html)
                proxys = []
                for msg in proxyMsg:
                    proxys.append(msg)
                return proxys
        except:
            print('从【无忧代理】获取数据失败')


def main():
    get_proxy = GetFreeProxy()
    for get_proxy_function in get_proxy.functions:
        proxys = get_proxy_function(get_proxy)
        print(proxys)


if __name__ == '__main__':
    main()
