# -*- coding: utf-8 -*-
import scrapy

# Spider、CrawlSpider
class BaiduSpider(scrapy.Spider):
    # 1. 爬虫名（必须）
    name = 'baidu'

    # 2. 允许爬虫抓取数据的域名范围（可选）
    allowed_domains = ['baidu.com']

    # 3. 启动爬虫后，发送的第一批url地址（这里的请求由引擎构建）
    start_urls = ['https://www.baidu.com/', 'https://tieba.baidu.com/']

    def parse(self, response):
        #print(response.url)
        file_name = response.xpath("//title/text()").extract_first()
        with open(file_name, "w") as f:
            f.write(response.body)



# spider  = BaiduSpider()
# spider.name
# spider.allowed_domains
# spider.start_urls

# for url in spider.start_urls:
#     response = downloader.send_request(url)

#     spider.parse(response)
