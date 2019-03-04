# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import os
import pymongo

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from settings import IMAGES_STORE

class DouyuImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(item['image_url'])
        #return [Request(item['image_url'])]

    def item_completed(self, results, item, info):
        # print("--" * 30)
        # print(results)
        # print('--' * 30)

        old_name = IMAGES_STORE + [x['path'] for ok, x in results if ok][0]
        new_name = IMAGES_STORE + item['nick_name'] + ".jpg"


        logging.info("Hello World!")

        try:
            os.rename(old_name, new_name)
            item['image_path'] = new_name
        except:
            logging.error("<{}> download failed".format(item['image_url']))

        return item

# [x for ok, x in results if ok]

# results = [
#     (
#         True,
#         {
#             'url': 'https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/21/5547decb995fee7fba3ac77f37546a89_small.jpg',
#             'path': 'full/4122a8e6a6cb9802da4d60f775528bd85b581f5f.jpg',
#             'checksum': '86d16540938cbd1fa970985318207df2'
#         }
#     )
# ]


class DouyuMongoPipeline(object):
    def open_spider(self, spider):
        self.coll = pymongo.MongoClient().douyu.item

    def process_item(self, item, spider):
        spider.logger.info("Hello world")
        self.coll.insert(dict(item))
        return item
