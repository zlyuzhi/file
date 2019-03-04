#coding:utf-8

import urllib2


def send_request():
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #"Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",

        # 重点：保存了登录信息的cookie
        "Cookie" : "anonymid=j7wsz80ibwp8x3; __utma=151146938.965194798.1536382787.1536382787.1536382787.1; __utmz=151146938.1536382787.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _r01_=1; depovince=GW; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20180921/1130/main_Affp_c9750000af421986.jpg; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; jebecookies=c48959c0-1d9d-4e32-9749-3677674ce7f3|||||; ick_login=8f659a2a-339b-4a2e-b325-7ad707cc4778; p=f70401fd70a59e9502778c30a22a80de9; first_login_flag=1; t=c23ce912d2206359c400585c3fad8c959; societyguester=c23ce912d2206359c400585c3fad8c959; id=327550029; xnsid=f88d2613; loginfrom=syshome; ch_id=10016; wp_fold=0",
        "Host" : "www.renren.com",
        "Referer" : "http://zhibo.renren.com/top",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }

    url_list = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile"
    ]

    for index, url in enumerate(url_list):
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)

        with open(str(index) + ".html", "w") as f:
            f.write(response.read())


if __name__ == '__main__':
    send_request()
