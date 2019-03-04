#coding:utf-8

try:
    from urllib.parse import unquote
except:
    from urllib import unquote

import scrapy

from ..items import AqiItem

class AqiSpider(scrapy.Spider):
    # 爬虫名
    name = "aqi_spider"
    # 允许抓取的域名范围
    allowed_domains = ["aqistudy.cn"]
    # 需要拼接的url部分
    base_url = "https://www.aqistudy.cn/historydata/"
    # 起始url地址，引擎会调用并发送请求，返回的响应交给 parse 解析
    start_urls = [base_url]

    def parse(self, response):
        """ 解析首页的响应 提取所有城市的链接 并发送请求 """

        # 提取所有城市链接  384
        city_link_list = response.xpath("//div[@class='all']//a/@href").extract()
        city_name_list = response.xpath("//div[@class='all']//a/text()").extract()

        #self.logger.info(city_link_list)

        for city_link, city_name in zip(city_link_list, city_name_list):
            # 发送每个城市链接的请求，并传递响应到 parse_month
            link = self.base_url + city_link
            yield scrapy.Request(link, meta={"city":city_name}, callback=self.parse_month)



    def parse_month(self, response):
        """解析每个城市的响应 提取所有月份的链接 并发送请求"""

        # 提取当前城市所有月的链接
        month_link_list = response.xpath("//tbody/tr/td[1]/a/@href").extract()

        #self.logger.info(month_link_list)

        for month_link in month_link_list[10:11]:
            # 发送每个月的链接请求，并传递响应到parse_day
            link = self.base_url + month_link
            yield scrapy.Request(link, meta=response.meta, callback=self.parse_day)


    def parse_day(self, response):
        """ 解析每个月的响应 提取所有天的数据 并保存在item中"""

        # 通过url提取城市名，并转为Unicode字符串
        # url = response.url
        # url_city = url[url.find("=")+1 : url.find("&")]
        # city_name = unquote(url_city).decode("utf-8")

        # 提取所有天的 tr 结点
        tr_list = response.xpath("//tbody/tr")
        # 删除第一个 表头tr
        tr_list.pop(0)

        city_name = response.meta['city']

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

