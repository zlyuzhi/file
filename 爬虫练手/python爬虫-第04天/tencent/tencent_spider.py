#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests
from bs4 import BeautifulSoup
import json


class TencentSpider(object):
    def __init__(self):
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.base_url = "https://hr.tencent.com/position.php?&start="
        self.page = 2750
        self.item_list = []


    def send_request(self, url):
        print("[INFO]: 正在发送请求 {}".format(url))
        response = requests.get(url, headers=self.headers)
        return response


    def parse_page(self, response):
        html = response.content
        soup = BeautifulSoup(html, "lxml")
        #html_obj = etree.HTML(html)

        # 提取所有tr结点的列表（每一页有10条信息，即10个tr结点）
        node_list = soup.find_all("tr", {"class" : ["even", "odd"]})
        #node_list = html_obj.xpath("//tr[@class='even'] | //tr[@class='odd']")

        # 迭代每一个结点，提取职位信息
        for node in node_list:
            # 每个item都保存一条职位信息
            item = {}
            # 职位名
            item['position_name'] = node.find_all("td")[0].a.text
            # 职位链接
            item['position_link'] = "https://hr.tencent.com/" + node.find_all("td")[0].a.get("href")
            # 职位类型
            item['position_type'] = node.find_all("td")[1].text
            # 招聘人数
            item['people_number'] = node.find_all("td")[2].text
            # 工作地点
            item['work_location'] = node.find_all("td")[3].text
            # 发布时间
            item['publish_times'] = node.find_all("td")[4].text
            # 将每个职位信息统一保存在同一个列表中
            self.item_list.append(item)

        # 判断当前页是否是最后一页，如果是直接return True（由外部while循环接收，并退出循环）
        if soup.find("a", {"class" : "noactive", "id" : "next"}):
          #html_obj.xpath("//a[@class='noactive' and @id='next']")
            return True
        else:
        # 如果不是最后一页，则正常提取下一页链接并返回（由外部while循环接收，并发送该url请求）
            next_link = "https://hr.tencent.com/" + soup.find("a", {"id" : "next"}).get("href")
            #next_link = "https://hr.tencent.com/" + html_obj.xpath("//a[@id='next']/@href")

            return next_link


    def save_data(self):
        # 不按Unicode处理，按当前Python解释器编码处理，并写入文件
        # 如果是Python3，默认解释器编码是 utf-8，可以正常写入
        # 如果是Python2，默认解释器编码是 ascii，则报 UnicodeEncodeError
        #   解决方案在代码文件顶部修改解释器编码为 utf-8 即可。
        json_str = json.dumps(self.item_list, ensure_ascii=False)
        with open("tencent.json", "w", ) as f:
            f.write(json_str)

        # json.dump(self.item_list, open("tencent.json", "w"))



    def main(self):
        # 第一个页面的url地址
        full_url = self.base_url + str(self.page)

        #while self.page <= 2800:
        while True:
            # 发送请求，返回响应
            response = self.send_request(full_url)
            # 解析响应，提取数据，并根据返回值决定是否退出循环
            full_url = self.parse_page(response)
            # 如果返回值是 True，则表示数据全部抓取完毕，可以退出循环
            if full_url == True:
                break
            #self.page += 10

        self.save_data()


if __name__ == '__main__':
    spider = TencentSpider()
    spider.main()
