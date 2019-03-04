#coding:utf-8

import time

from selenium import webdriver

# from scrapy import Request
# from scrapy import Item
from scrapy.http import HtmlResponse

from retrying import retry



class AqiSeleniumMiddleware(object):
    def __init__(self):
        # 有界面的Chrome
        #self.driver = webdriver.Chrome()

        # 无界面浏览器（无头浏览器）不再显示图形界面，比有界面要快一些
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=self.options)



    # 显式等待（判断页面数据是否出现，如果出现则继续执行，如果没出现则继续等待）
    # 隐式等待（固定等待时间）

    # retry_load_page() 是一个自定义方法，用来判断页面指定数据是否渲染成功

    # @retry(stop_max_attempt_number=40, wait_fixed=100) 是一个retry装饰器，捕获方法的异常，进行重试操作，最大重试40次，每次重试间隔100毫秒：

    # 1. 如果retry_load_page()方法 执行时没有异常，表示页面数据渲染成功，则retry不会工作，程序正常向后执行；
    # 2. 如果retry_load_page()方法 执行时有异常，表示页面数据渲染失败，则retry捕获异常，进行重试：
    #  -a. 如果在40次重试内，方法不再抛出异常，表示页面数据渲染成功，则retry不再工作，程序正常向后执行；
    #  -b. 如果在40次重试后，方法依然抛出异常，则retry不再捕获异常，异常抛出给调用处处理。

    @retry(stop_max_attempt_number=20, wait_fixed=200)
    def retry_load_page(self, request, spider):
        try:
            # 判断页面数据是否出现，如果出现则正常执行；如果没出现则抛出异常由 try 捕获
            self.driver.find_element_by_xpath("//tbody/tr/td[1]")
        except:
            # 每次出现异常，记录重试次数，并 raise 手动抛出异常让 retry装饰器工作
            spider.logger.debug("Retry <{}> {} times.".format(request.url, self.num))
            self.num += 1
            raise Exception("<{}> page loading failed.".format(request.url))


    def process_request(self, request, spider):
        if "monthdata" in request.url or "daydata" in request.url:
            # 发送浏览器请求
            self.driver.get(request.url)
            self.num = 1

            try:
                # 显式等待（判断页面数据是否出现，如果出现则继续执行，如果没出现则继续等待）
                self.retry_load_page(request, spider)
                # 隐式等待（固定等待时间）
                #time.sleep(2)
                # 获取网页 Unicode 编码字符串
                html = self.driver.page_source
                # 构建一个scrapy的response响应对象
                response = HtmlResponse(url=self.driver.current_url, body=html.encode("utf-8"), encoding="utf-8", request=request)
                # 返回响应对象给引擎，引擎会交给spider解析
                return response
            except Exception as e:
                spider.logger.error(e)



    def __del__(self):
        self.driver.quit()

        # response.body
        # #response.text
        # response.url
        # response.encoding
        # response.request

        # response.meta = request.meta

        # response.xpath()


