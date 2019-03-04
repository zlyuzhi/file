#coding:utf-8


import urllib2
import random

def send_request():
    url = "http://httpbin.org/ip"

    proxy_list = [
        {"http":"http://maozhaojun:ntkn0npx@39.106.10.232:16818"},
        {}
    ]

    proxy = random.choice(proxy_list)

    # 1. 构建代理处理器对象
    proxy_handler = urllib2.ProxyHandler(proxy)
    # 2. 使用代理处理器，构建opener
    opener = urllib2.build_opener(proxy_handler)
    # 3. 使用opener发送请求，即可使用代理
    response = opener.open(url)

    print(response.read())


if __name__ == '__main__':
    send_request()
