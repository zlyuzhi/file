# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class AllItem(scrapy.Item):
    """
        将多个页面的所有数据全部存在一起
    """

    # 职位名
    position_name = scrapy.Field()
    # 职位链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()
    # 工作职责
    position_zhize = scrapy.Field()
    # 工作要求
    position_yaoqiu = scrapy.Field()


class TencentItem(scrapy.Item):
    """
        列表页数据字段
    """

    # 职位名
    position_name = scrapy.Field()
    # 职位链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()


class PositionItem(scrapy.Item):
    """
        详情页数据字段
    """
    # 工作职责
    position_zhize = scrapy.Field()
    # 工作要求
    position_yaoqiu = scrapy.Field()





