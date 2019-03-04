#coding:utf-8

import json


from ..items import DouyuItem
import scrapy


class DouyuSpider(scrapy.Spider):
    name = "douyu2"

    allowed_domains = ["douyucdn.cn"]


    baes_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    page = 0
    start_urls = [baes_url + str(page)]


    def parse(self, response):
        # 提取json响应的data字段数据
        data_list = json.loads(response.body)['data']

        # 判断data_list是否有数据，如没有数据，则退出parse方法
        if not data_list:
            return

        for data in data_list:
            item = DouyuItem()
            item['room_url'] = "http://www.douyu.com/" + data['room_id']
            item['image_url'] = data['vertical_src']
            item['nick_name'] = data['nickname']
            item['city'] = data['anchor_city']

            yield item

        self.logger.info("room url")
        self.logger.info(item['room_url'])

        # 发送json文件的翻页请求
        self.page += 100
        yield scrapy.Request(self.baes_url + str(self.page), callback=self.parse)



