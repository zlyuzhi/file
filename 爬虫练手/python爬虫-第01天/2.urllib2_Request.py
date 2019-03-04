#coding:utf-8

import urllib2


def send_request():

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Connection": "keep-alive"
    }

    # 构建一个包含请求报头的请求对象
    request = urllib2.Request("http://www.baidu.com/", headers=headers)

    # 发送指定的url地址请求，返回一个类文件的响应对象
    response = urllib2.urlopen(request)
    # 读取响应中内容，获取网页原始编码字符串
    html = response.read()

    return html


if __name__ == '__main__':
    html = send_request()

    with open("baidu.html", "w") as f:
        f.write(html)
