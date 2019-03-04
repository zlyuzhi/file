#coding:utf-8

#import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = "tencent_crawl"

    allowed_domains = ["hr.tencent.com"]

    # starturls做为第一批请求发送出去，返回的响应默认follow=True，所以一定会经过rules的每个Rule处理
    start_urls = ["https://hr.tencent.com/position.php?&start=0"]


    rules = [
        Rule(LinkExtractor(allow=r'start=\d+'), follow=True),

        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'), callback="parse_page")
    ]

    def parse_page(self, response):
        #item = response.meta["item"]
        item = {}

        item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()

        item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item

