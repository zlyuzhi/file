# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from alidata.alidata.items import AwsItem


class AlidataPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,AwsItem):
            #把它存入数据库
            pass
        return item

