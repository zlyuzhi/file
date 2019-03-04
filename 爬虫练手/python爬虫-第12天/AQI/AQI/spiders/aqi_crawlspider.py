#coding:utf-8

try:
    from urllib.parse import unquote
except:
    from urllib import unquote

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import AqiItem


class AqiCrawlSpider(CrawlSpider):
    name = "aqi_crawlspider"

    # 允许抓取的域名范围
    allowed_domains = ["aqistudy.cn"]
    # 需要拼接的url部分
    base_url = "https://www.aqistudy.cn/historydata/"
    # 起始url地址，引擎会调用并发送请求，返回的响应交给 rules进行提取链接
    start_urls = [base_url]

    rules = [
        # 从start_urls的响应中，提取所有城市的链接，并发送每个城市链接的请求，返回的响应需要继续提取链接
        Rule(LinkExtractor(allow=r"monthdata\.php\?city="), follow=True),
        # 从每个城市的响应中，提取所有月份的链接，并发送每个月的链接请求，返回的响应交给callback解析该月的所有天数据
        Rule(LinkExtractor(allow=r"daydata\.php\?city="), callback="parse_day", follow=False)
    ]


    def parse_day(self, response):
        """ 解析每个月的响应 提取所有天的数据 并保存在item中"""

        # 通过url提取城市名，并转为Unicode字符串
        url = response.url
        url_city = url[url.find("=")+1 : url.find("&")]
        city_name = unquote(url_city).decode("utf-8")

        # 提取所有天的 tr 结点
        tr_list = response.xpath("//tbody/tr")
        # 删除第一个 表头tr
        tr_list.pop(0)

        # 获取每天的数据并保存到item中
        for tr in tr_list:
            item = AqiItem()
            item['city'] = city_name
            # 日期
            item['date'] = tr.xpath("./td[1]/text()").extract_first()
            # AQI
            item['aqi'] = tr.xpath("./td[2]/text()").extract_first()
            # 质量等级
            item['level'] = tr.xpath("./td[3]/span/text()").extract_first()
            # PM2.5
            item['pm2_5'] = tr.xpath("./td[4]/text()").extract_first()
            # PM10
            item['pm10'] = tr.xpath("./td[5]/text()").extract_first()
            # SO2
            item['so2'] = tr.xpath("./td[6]/text()").extract_first()
            # CO
            item['co'] = tr.xpath("./td[7]/text()").extract_first()
            # NO2
            item['no2'] = tr.xpath("./td[8]/text()").extract_first()
            # O3_8h
            item['o3'] = tr.xpath("./td[9]/text()").extract_first()

            yield item

