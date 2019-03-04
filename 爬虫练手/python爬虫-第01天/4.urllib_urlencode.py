#coding:utf-8


import urllib
import urllib2

def send_request():
    #输入自定义查询的关键字
    keyword = raw_input("请输入需要查询的关键字")
    # 固定的url地址
    base_url = "https://www.baidu.com/s?"

    # 构建查询字典
    query_dict = {"wd" : keyword}
    # 通过urlencode方法，构建查询字符串
    query_str = urllib.urlencode(query_dict)

    # 和固定的url地址拼接，构建完整的url地址
    full_url = base_url + query_str

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    reqeust = urllib2.Request(full_url, headers=headers)

    response = urllib2.urlopen(reqeust)

    return response.read()


if __name__ == '__main__':
    html = send_request()
    with open("baidu.html", "w") as f:
        f.write(html)
