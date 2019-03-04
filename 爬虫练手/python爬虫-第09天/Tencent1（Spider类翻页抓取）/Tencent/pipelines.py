# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TencentPipeline(object):
    #def __init__(self):
    def open_spider(self, spider):
        self.coll = pymongo.MongoClient().tencent.list


    def process_item(self, item, spider):
        self.coll.insert(dict(item))
        return item

    def close_spider(self, spider):
        #self.coll.close()
        pass



