# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduJsonPipeline(object):
    def process_item(self, item, spider):
        return item


class BaiduCsvPipeline(object):
    def process_item(self, item, spider):
        return item


class BaiduMongoDBPipeline(object):
    def process_item(self, item, spider):
        return item
