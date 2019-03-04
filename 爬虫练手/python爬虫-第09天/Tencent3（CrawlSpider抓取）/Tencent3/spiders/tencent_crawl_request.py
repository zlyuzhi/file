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
        Rule(LinkExtractor(allow=r'start=\d+'), callback="parse_item", follow=True)

        #Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'), callback="parse_page")
    ]

    def parse_item(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencentItem()
            # 职位名
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            # 详情链接
            item['position_link'] = "https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            # 职位类型
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            # 招聘人数
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            # 工作地点
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            #发布时间
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()

            # 每次迭代提取一组数据item，通过yield 交给引擎-管道
            yield item

            yield scrapy.Request(item['position_link'], callback=self.parse_page, meta)



    def parse_page(self, response):
        #item = response.meta["item"]
        item = {}

        item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()

        item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item

