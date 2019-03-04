item#coding:utf-8

import time
import unittest

from selenium import webdriver
from lxml import etree
import pymongo


class DouyuSpider(unittest.TestCase):
    #def __init__(self)  构造方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.collection = pymongo.MongoClient().douyu.directory


    def testDouyu(self):
        # 在浏览器地址栏输入第一页的url地址
        self.driver.get("https://www.douyu.com/directory/all")

        while True:
            # 获取当前页面的网页源码
            html = self.driver.page_source
            html_obj = etree.HTML(html)
            # 获取所有主播结点的列表
            node_list = html_obj.xpath("//div[@id='live-list-content']//div[@class='mes']")

            for node in node_list:
                item = {}
                try:
                    item["room_name"] = node.xpath('.//h3[@class="ellipsis"]/text()')[0].strip()
                except:
                    item["room_name"] = None

                if node.xpath('.//span[@class="tag ellipsis"]/text()'):
                    item["type_name"] = node.xpath('.//span[@class="tag ellipsis"]/text()')[0].strip()
                else:
                    item["type_name"] =  None

                item["directory_name"] = node.xpath('.//span[@class="dy-name ellipsis fl"]/text()')[0].strip()

                item["people_number"] = node.xpath('.//span[@class="dy-num fr"]/text()')[0].strip() if node.xpath('.//span[@class="dy-num fr"]/text()') else None


                self.collection.insert(item)

            # 判断当前页面是否是最后一页，如果是则break退出循环
            if "shark-pager-next shark-pager-disable shark-pager-disable-next" in html:
                break
            # 每次循环，点击下一页链接
            self.driver.find_element_by_class_name("shark-pager-next").click()
            time.sleep(1)

    #def __del__(self) 析构方法
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
