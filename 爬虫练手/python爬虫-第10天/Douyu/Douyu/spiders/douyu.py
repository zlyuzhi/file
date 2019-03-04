#coding:utf-8

import json


from ..items import DouyuItem
import scrapy


class DouyuSpider(scrapy.Spider):
    name = "douyu"

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

            # 发送图片请求，并传递item到 指定的回调函数里
            yield scrapy.Request(item['image_url'], meta={"item":item}, callback=self.parse_image)

        # 发送json文件的翻页请求
        self.page += 100
        yield scrapy.Request(self.baes_url + str(self.page), callback=self.parse)


    def parse_image(self, response):
        item = response.meta["item"]

        # 指定当前图片的存储路径和文件名
        file_name = "/Users/Power/lesson_python/_19_0731/day10/Douyu/Douyu/data/" + item['nick_name'] + ".jpg"

        # 将图片的路径保存在item字段里
        item["image_path"] = file_name

        # 保存图片
        with open(file_name, "wb") as f:
            f.write(response.body)

        # 将item交给管道处理
        yield item








