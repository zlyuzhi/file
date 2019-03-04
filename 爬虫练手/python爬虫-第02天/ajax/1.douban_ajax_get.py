#coding:utf-8


import urllib
import urllib2

import json
# json.loads() : 将 json字符串 转为对应的 Python数据类型
# json.dumps() : 将Python数据类型 转为对应的 Json字符串

def send_request():
    # json文件的url地址，通过抓包得到的
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

    # 请求报头
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}


    start = 0
    while True:
        # 构建查询字符串
        query_dict = {"start" : start, "limit" : "100"}
        query_str = urllib.urlencode(query_dict)

        # 拼接url地址
        url = base_url + query_str

        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        # response的read()方法只能执行一次，后续执行则没有数据
        # read() 取值是 json 字符串
        json_str = response.read()

        # json.loads() 将json字符串转为Python数据类型
        if not json.loads(json_str):
            break

        print(json_str)

        start += 50


if __name__ == '__main__':
    send_request()
