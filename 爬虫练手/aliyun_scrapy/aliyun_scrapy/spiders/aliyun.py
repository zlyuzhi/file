# -*- coding: utf-8 -*-
# https://www.cnblogs.com/strivepy/p/9614721.html
import scrapy
from scrapy import Request
from selenium import webdriver


class AliyunSpider(scrapy.Spider):
    name = 'aliyun'
    # allowed_domains = ['aliyun.com']
    # start_urls = ['https://www.aliyun.com/price/detail/ecsnew#/?_k=brx1w3']
    # start_urls = ['https://www.baidu.com']

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)

    def start_requests(self):
        start_requests = ["https://www.aliyun.com/price/detail/ecsnew#/?_k=brx1w3"]
        for url in start_requests:
            yield Request(url=url,callback=self.parse)

    def parse(self, response):

        page_source = response.body.decode()
        results = page_source.xpath("//tbody")
        for result in results:
            tds = result.xpath("./tr//td/text()").extract()

        # print(response.body.decode())
