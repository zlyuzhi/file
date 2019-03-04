#coding:utf-8


import scrapy
#from ITCast.items import ItcastItem
from ..items import ItcastItem


class ItcastSpider(scrapy.Spider):

    # 爬虫名
    name = "itcast"
    # 允许抓取的域名范围（防止爬虫失控）
    allowed_domains = ['itcast.cn']
    # 起始url地址列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']


    def parse(self, response):


        node_list = response.xpath("//div[@class='li_txt']")

        for node in node_list:
            #item = {}
            # 每个item表示一组数据
            item = ItcastItem()

            item['name'] = node.xpath("./h3/text()").extract_first()
            item['title'] = node.xpath("./h4/text()").extract_first()
            item['info'] = node.xpath("./p/text()").extract_first()

            #return item
            # 每次循环返回item数据给引擎，由引擎交给管道处理
            yield item

            # 如果执行爬虫命令 scrapy crawl itcast -o itcast.json
            # 则使用scrapy提供的数据存储（json、csv、xml、jl等）



# response = downloader.send_request(url)

# for item in spider.parse(response):
#     pipeline.process_item(item, spider)


