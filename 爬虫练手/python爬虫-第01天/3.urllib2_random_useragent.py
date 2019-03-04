#coding:utf-8

import random
import urllib2


USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"
]

def send_request():

    # UserAgent池、IP代理池、Cookie池
    # 通过random.choice随机从列表中返回一个新的useragent
    useragent = random.choice(USER_AGENT_LIST)

    # headers = {
    #     "User-Agent" : useragent,
    # }

    # 构建一个包含请求报头的请求对象
    #request = urllib2.Request("http://www.baidu.com/", headers=headers)
    request = urllib2.Request("http://www.baidu.com/")


    # 添加/修改 指定请求报头值
    request.add_header("User-Agent", useragent)

    # 获取指定请求报头值
    print(request.get_header("User-agent"))

    # 发送指定的url地址请求，返回一个类文件的响应对象
    response = urllib2.urlopen(request)

    # 获取响应的状态码
    if response.getcode() == 200:
        # 读取响应中内容，获取网页原始编码字符串
        html = response.read()

        return html
    return None


if __name__ == '__main__':
    html = send_request()

    with open("baidu.html", "w") as f:
        f.write(html)
