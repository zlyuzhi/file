# -*- coding: utf-8 -*-
import scrapy


class AliSpider(scrapy.Spider):
    name = 'ali'
    allowed_domains = ['aliyun.com']
    start_urls = ['http://aliyun.com/']

    def parse(self, response):
        pass
