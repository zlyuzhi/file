#coding:utf-8

import urllib2


def send_request():

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    # 1. 构建特定功能的处理器对象
    http_handler = urllib2.HTTPHandler()
    # 2. 使用处理器对象，构建自定义opener，这个opener发送会附带处理器功能
    opener = urllib2.build_opener(http_handler)
    # 3. 使用opener的open()方法发送请求即可
    response = opener.open(request)
    #response = opener.open("http://www.baidu.com/")
    #response = urllib2.urlopen("http://www.baidu.com/")

    print(response.read())


if __name__ == '__main__':
    send_request()
