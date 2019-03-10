# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# https://blog.csdn.net/zhan006/article/details/84107542
class AlidataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name =scrapy.Field()
    startard=scrapy.Field()
    cpu=scrapy.Field()
    price_month=scrapy.Field()

class AwsItem(scrapy.Item):
    name=scrapy.Field()
    memory =scrapy.Field()


