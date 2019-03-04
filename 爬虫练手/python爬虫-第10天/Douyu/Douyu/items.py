# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 直播间url
    room_url = scrapy.Field()
    # 图片url
    image_url = scrapy.Field()
    # 昵称
    nick_name = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片磁盘路径
    image_path = scrapy.Field()
