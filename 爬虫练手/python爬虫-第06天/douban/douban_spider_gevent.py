#coding:utf-8

import time
try:
    from Queue import Queue
except:
    from queue import Queue

import gevent
from gevent import monkey
from gevent.pool import Pool

import requests
from lxml import etree

monkey.patch_all()

class DoubanSpider(object):
    def __init__(self):
        self.url_list = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.queue = Queue()


    def send_request(self, url):
        print("[INFO]: send requests {}".format(url))
        response = requests.get(url, headers=self.headers)
        time.sleep(1)
        return response


    def parse_page(self, response):
        html = response.content
        html_obj = etree.HTML(html)
        node_list = html_obj.xpath("//div[@class='info']")

        for node in node_list:
            title = node.xpath("./div[1]/a/span[1]/text()")[0]
            score = node.xpath(".//span[@class='rating_num']/text()")[0]

            self.queue.put(title + "\t" + score)


    def main(self):
        # for url in self.url_list:
        #     response = self.send_request(url)
        #     self.parse_page(response)


        #  协程任务

        # job_list = []
        # for url in self.url_list:
        #     job = gevent.spawn(self.send_request, url)
        #     job_list.append(job)

        # # 返回执行后的协程对象列表
        # g_list = gevent.joinall(job_list)

        # for g in g_list:
        #     # g.get() 获取response
        #     self.parse_page(g.get())


        _ = [self.parse_page(g.get()) for g in gevent.joinall([gevent.spawn(self.send_request, url) for url in self.url_list])]


        # 协程池

        # pool = Pool()
        # for url in self.url_list:
        #     pool.apply_async(self.send_request, args=[url], callback=self.parse_page)

        # # 让主线程
        # pool.join()


if __name__ == '__main__':
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    end = time.time()
    # 3 sec
    print("[INFO]: using time {}".format(end - start))
