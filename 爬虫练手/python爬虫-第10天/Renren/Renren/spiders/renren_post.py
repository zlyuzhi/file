# -*- coding: utf-8 -*-
import scrapy
import requests


class RenrenPostSpider(scrapy.Spider):
    name = 'renren_post'
    allowed_domains = ['renren.com']
    #start_urls = ["http://www.renren.com/PLogin.do"]

    def start_requests(self):
        """
            发送登录页面的post请求，提交账户密码，如果登录成功，scrapy会记录登录状态的cookie，并自动传递
        """
        post_url = "http://www.renren.com/PLogin.do"

        form_dict = {
            "email" : "mr_mao_hacker@163.com",
            "password" : "ALARMCHIME"
        }

        yield scrapy.FormRequest(url=post_url, formdata=form_dict, callback=self.parse)


    def parse(self, response):
        """
            附带scrapy保存的cookie，发送其他页面的get请求，获取响应交给callback解析
        """
        url_list = [
            'http://www.renren.com/327550029/profile',
            'http://www.renren.com/410043129/profile'
        ]

        for url in url_list:
            yield scrapy.Request(url, callback=self.parse_page)


    def parse_page(self, response):
        """
            解析响应，提取数据
        """
        title = response.xpath("//title/text()").extract_first()

        with open(title + ".html", "w") as f:
            f.write(response.body)



