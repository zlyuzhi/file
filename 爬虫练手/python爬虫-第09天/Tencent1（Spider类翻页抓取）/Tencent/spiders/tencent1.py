#coding:utf-8

import scrapy
from ..items import TencentItem

class TencentSpider(scrapy.Spider):

    #scrapy genspider tencent hr.tencent.com

    name = "tencent1"

    allowed_domains = ["hr.tencent.com"]

    # python3可能会出现无法取到类属性，所以通过 global
    #global base_url, page
    base_url = "https://hr.tencent.com/position.php?&start="
    page = 0

    start_urls = [base_url + str(page)]

    def parse(self, response):
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


        if self.page <= 100:
            self.page += 10
            # scrapy.Request(item['position_link'], callback=self.parse_page)

            # 构建一个请求并交给引擎-调度器-下载器发送请求，并响应传递给callback指定的回调函数解析
            yield scrapy.Request(url=self.base_url + str(self.page), callback=self.parse)



    # def parse_page(self, response):
    #     url = resoonse.xpath()
    #     scrapy.Request(url, callback=self.parse)


