# coding:utf-8


import requests
# lxml是类库，etree是模块
from lxml import etree
# from PIL import Image


class TiebaSpider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.base_url = "http://tieba.baidu.com"

        self.tieba_name = input("请输入需要抓取的贴吧名：")
        self.begin_page = int(input("请输入需要抓取的起始页："))
        self.end_page = int(input("请输入需要抓取的结束页："))

    def send_request(self, url, query_dict={}):
        response = requests.get(url, params=query_dict, headers=self.headers)
        return response

    def parse_page(self, response):
        html = response.content
        # print(html)
        html_obj = etree.HTML(html)
        page_link_list = html_obj.xpath("//a[@class='j_th_tit ']/@href")
        return page_link_list

    def parse_image(self, response):
        html = response.content

        html_obj = etree.HTML(html)
        image_link_list = html_obj.xpath("//img[@class='BDE_Image']/@src")
        return image_link_list

    def save_image(self, response, filename):
        print("[INFO]: 正在保存图片 {}".format(filename))
        with open(filename, "wb") as f:
            f.write(response.content)

    def main(self):
        # 帖子列表页数据抓取 提取 每个帖子链接
        # for page in range(self.begin_page, self.end_page + 1):
        for page in range(1, 11):
        for page in [1,2,3,4...10]
            pn = (page - 1) * 50

            query_dict = {"kw": self.tieba_name, "pn": pn}
            full_url = self.base_url + "/f?"

            response = self.send_request(full_url, query_dict)
            page_link_list = self.parse_page(response)

            # 帖子详情页数据抓取 提取 每个图片链接
            for page_link in page_link_list:
                page_full_url = self.base_url + page_link
                page_response = self.send_request(page_full_url)

                image_link_list = self.parse_image(page_response)

                # 图片数据抓取并保存
                for image_link in image_link_list:
                    image_response = self.send_request(image_link)

                    self.save_image(image_response, image_link[-15:])



if __name__ == '__main__':
    spider = TiebaSpider()
    spider.main()
