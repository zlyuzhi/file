#coding:utf-8

import time
try:
    from Queue import Queue
except:
    from queue import Queue
# 导入多进程模块里的线程池
from multiprocessing.dummy import Pool

import requests
from lxml import etree


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
        pool = Pool(10)
        # response_list = pool.map(self.send_request, self.url_list)

        # for response in response_list:
        #     self.parse_page(response)

        for url in self.url_list:
            response = pool.apply(self.send_request, args=[url])
            self.parse_page(response)

        # 关闭线程池，不再接受新的线程任务
        pool.close()
        # 让主线程阻塞，等待所有子线程执行结束
        pool.join()





if __name__ == '__main__':
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    end = time.time()
    # 3 sec
    print("[INFO]: using time {}".format(end - start))
