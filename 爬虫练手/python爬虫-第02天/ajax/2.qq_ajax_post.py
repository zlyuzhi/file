#coding:utf-8

import urllib
import urllib2
import time
import json


def send_request():
    # 通过抓包找到的 post请求的url地址
    post_url = "https://fanyi.qq.com/api/translate"

    headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",

        # 表示客户端支持的压缩格式，urllib2不支持gzip解压，但是requests和scrapy默认支持gzip解压。
        #"Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection" : "keep-alive",

        # 传递的表单数据的长度
        "Content-Length" : "285",

        # 传递的表单数据，是通过urlencode转码后
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",

        "Cookie" : "pgv_pvi=718218240; RK=kO8/hNauMo; ptcz=8a6aa2eb109c92d6aa94aa7cc0aece1190b73987b80cc71037c056b024920137; pt2gguin=o0123636274; tvfe_boss_uuid=f21d3a8294e89358; mobileUV=1_15f9f25154c_a6c21; pgv_pvid=1030544080; o_cookie=123636274; pac_uid=1_123636274; fy_guid=9b09602e-d2ed-4797-930d-a8054582a349; ts_uid=5628386130; gr_user_id=eeb2afb3-d0b6-4e0c-ac3e-95568013e7b5; grwng_uid=3840cabe-39e3-4067-a18c-0162a15f374c; qtv=e8fbdcdd4cdfc789; qtk=hZ0SKxtrrKHrmuPTyRiOGSmx0YlAWAMxomxdEG5i54X+BhnrpM+zZJtSxxWNSHzkXBMCXQWgQhj7r6uthSbnndMokR1P/H/H+nPPNnO90Veu/7v46adMihj380KSpqXENEqkmSplLo3CApiarKroNQ==; pgv_info=ssid=s4222111224; ts_last=fanyi.qq.com/; openCount=1; 9c118ce09a6fa3f4_gr_session_id=dc51827c-e947-499f-af15-b4f6ac276938; 9c118ce09a6fa3f4_gr_session_id_dc51827c-e947-499f-af15-b4f6ac276938=true",
        "Host" : "fanyi.qq.com",
        "Origin" : "https://fanyi.qq.com",
        "Referer" : "https://fanyi.qq.com/",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        # 表示是ajax请求
        "X-Requested-With" : "XMLHttpRequest"
    }


    # 构建表单数据
    form_dict = {
        "source" : "auto",
        "target" : "auto",
        "sourceText" : raw_input("请输入需要翻译的文本："),
        # qtv和qtk对应Cookie里的qtv和qtv
        "qtv" : "e8fbdcdd4cdfc789",
        "qtk" : "hZ0SKxtrrKHrmuPTyRiOGSmx0YlAWAMxomxdEG5i54X+BhnrpM+zZJtSxxWNSHzkXBMCXQWgQhj7r6uthSbnndMokR1P/H/H+nPPNnO90Veu/7v46adMihj380KSpqXENEqkmSplLo3CApiarKroNQ==",
        # 这个数据字段根据UNIX时间戳处理
        "sessionUuid" : "translate_uuid" + str(int(time.time() * 1000))
    }
    form_data = urllib.urlencode(form_dict)

    # 根据表单数据，更改Content-Length 长度
    headers['Content-Length'] = len(form_data)

    # 这是一个有表单数据的 post请求对象
    request = urllib2.Request(post_url, form_data, headers)
    response = urllib2.urlopen(request)

    # 将json字符串转为对应的Python数据类型
    json_data = json.loads(response.read())

    # 取出最后的翻译结果
    trans_text = json_data['translate']['records'][0]['targetText']
    print(trans_text)


if __name__ == '__main__':
    send_request()
