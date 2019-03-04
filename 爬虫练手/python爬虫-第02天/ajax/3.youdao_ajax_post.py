#coding:utf-8


import urllib
import urllib2
import json
import hashlib
import random
import time


def get_token():

    # 需要翻译的文本
    text = raw_input("请输入需要翻译的文本：")
    # 计算的 salt值
    salt = str(int(time.time() * 1000) + random.randint(0, 10))
    # 计算的sign值，通过md5生成
    sign = hashlib.md5("fanyideskweb" + text + salt + "sr_3(QOHT)L2dx#uuGR@r").hexdigest()

    return (text, salt, sign)

def send_request():
    # post请求的url地址
    post_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    # 请求报头
    headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection" : "keep-alive",
        "Content-Length" : "218",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie" : "_ntes_nnid=f77d53cb936304b5333b304b767a4958,1506087321856; OUTFOX_SEARCH_USER_ID_NCOO=971893961.4325761; OUTFOX_SEARCH_USER_ID=-1480774266@10.169.0.83; JSESSIONID=aaaQmuijs-T6c-5zUhhCw; ___rl__test__cookies=1542014113529",
        "Host" : "fanyi.youdao.com",
        "Origin" : "http://fanyi.youdao.com",
        "Referer" : "http://fanyi.youdao.com/",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "X-Requested-With" : "XMLHttpRequest"
    }

    # 计算得出的加密参数
    text, salt, sign = get_token()

    # 构建表单数据
    form_dict = {
        "i" : text,
        "from" : "AUTO",
        "to" : "AUTO",
        "smartresult" : "dict",
        "client" : "fanyideskweb",
        "salt" : salt,
        "sign" : sign,
        "doctype" : "json",
        "version" : "2.1",
        "keyfrom" : "fanyi.web",
        "action" : "FY_BY_CLICKBUTTION",
        "typoResult" : "false",
    }
    form_data = urllib.urlencode(form_dict)
    # 修改content-length值
    headers["Content-Length"] = len(form_data)

    # 构建post请求发送，并获取响应（json字符串）
    request = urllib2.Request(post_url, form_data, headers)
    response = urllib2.urlopen(request)

    # 将json字符串转为对应的Python数据类型
    json_data = json.loads(response.read())
    # 获取翻译结果
    trans_text = json_data["translateResult"][0][0]["tgt"]
    print(trans_text)


if __name__ == '__main__':
    send_request()
