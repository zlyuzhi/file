# -*- coding: utf-8 -*-
import scrapy


class RenrenCookiesSpider(scrapy.Spider):
    name = 'renren_cookies'
    allowed_domains = ['renren.com']

    start_urls = [
        'http://www.renren.com/327550029/profile',
        'http://www.renren.com/410043129/profile'
    ]

    def start_requests(self):

        headers = {
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding" : "gzip, deflate",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control" : "max-age=0",
            "Connection" : "keep-alive",
            "Host" : "www.renren.com",
            "Referer" : "http://zhibo.renren.com/top",
            "Upgrade-Insecure-Requests" : "1",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }

        cookies = {
            "anonymid" : "j7wsz80ibwp8x3",
            "__utma" : "151146938.965194798.1536382787.1536382787.1536382787.1",
            "__utmz" : "151146938.1536382787.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
            "_r01_" : "1",
            "ln_uact" : "mr_mao_hacker@163.com",
            "ln_hurl" : "http://hdn.xnimg.cn/photos/hdn321/20180921/1130/main_Affp_c9750000af421986.jpg",
            "depovince" : "GW",
            "ick_login" : "bb4b95e6-d6ff-4f4e-be4b-103290ff8e80",
            "first_login_flag" : "1",
            "loginfrom" : "syshome",
            "ch_id" : "10016",
            "jebecookies" : "8a6fb168-8007-4e55-b467-255ee8a08209|||||",
            "JSESSIONID" : "abc8_tSgz8mLWdhtMojDw",
            "_de" : "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
            "p" : "063f996be0db6c12e2ffdfb07f2420dc9",
            "t" : "ca6fe3b237702b40b4e084785f5e46d79",
            "societyguester" : "ca6fe3b237702b40b4e084785f5e46d79",
            "id" : "327550029",
            "xnsid" : "b6c57be0"
        }

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, cookies=cookies, callback=self.parse)


    def parse(self, response):
        title = response.xpath("//title/text()").extract_first()

        with open(title + ".html", "w") as f:
            f.write(response.body)


