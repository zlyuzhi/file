# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json

class ItcastJsonPipeline(object):
    #def __init__(self):
    # 爬虫启动时，执行一次
    def open_spider(self, spider):
        self.f = open("itcast.json", "w")

    # 每次由引擎传入一个item，则执行一次
    def process_item(self, item, spider):

        # item['spider'] = spider.name
        # item['time'] = str(datetime.datetime.now())

        json_str = json.dumps(dict(item)) + "\n"
        self.f.write(json_str)

        # 将处理后的item返回给引擎，由引擎交给下一个管道处理
        return item

    # 爬虫结束时，执行一次
    def close_spider(self, spider):
        self.f.close()






# pipeline = ItcastPipeline()

# pipelines.open_spider(spdier)

# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)
# pipelines.process_item(item, spider)

# pipelines.close_spider(spider)
