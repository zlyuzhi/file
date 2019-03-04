#coding:utf-8

import urllib2


def send_request():
    # 发送指定的url地址请求，返回一个类文件的响应对象
    response = urllib2.urlopen("http://www.baidu.com/")
    # 读取响应中内容，获取网页原始编码字符串
    html = response.read()

    return html


if __name__ == '__main__':
    html = send_request()

    with open("baidu.html", "w") as f:
        f.write(html)
