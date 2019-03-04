# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from items import TencentItem, PositionItem

import pymongo


class TencentAllPipeline(object):
    def open_spider(self, spider):
        self.coll = pymongo.MongoClient().tencent.all

    def process_item(self, item, spider):
        #if isinstance(item, TencentItem):
        self.coll.insert(dict(item))
        return item


class TencentListPipeline(object):
    def open_spider(self, spider):
        self.coll = pymongo.MongoClient().tencent.list

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            self.coll.insert(dict(item))

        return item

class TencentDetailPipeline(object):
    def open_spider(self, spider):
        self.coll = pymongo.MongoClient().tencent.detail

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            self.coll.insert(dict(item))

        return item
