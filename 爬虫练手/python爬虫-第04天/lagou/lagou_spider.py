#coding:utf-8

import json

import requests
from jsonpath import jsonpath


class LagouSpider(object):
    def __init__(self):
        self.headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection" : "keep-alive",
            "Content-Length" : "25",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie" : "user_trace_token=20170923184359-1ba5fe6f-a04c-11e7-a60e-525400f775ce; LGUID=20170923184359-1ba6010d-a04c-11e7-a60e-525400f775ce; _ga=GA1.2.136733168.1506163440; _gid=GA1.2.1817431977.1542253084; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAGGABCB7F613FC0F51CAA33DF26E0E75306A26D; LGSID=20181115172902-e3666046-e8b8-11e8-9f7e-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542253085,1542274142; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542274641; LGRID=20181115173720-0caa6b7e-e8ba-11e8-9f7f-525400f775ce; SEARCH_ID=b19bd022583241c883c3f0bc93cf6d3e",
            "Host" : "www.lagou.com",
            "Origin" : "https://www.lagou.com",
            # 1. 反爬检查1
            "Referer" : "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
            # 2. 反爬检查2
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "X-Anit-Forge-Code" : "0",
            "X-Anit-Forge-Token" : "None",
            "X-Requested-With" : "XMLHttpRequest"
        }
        self.post_url = "https://www.lagou.com/jobs/positionAjax.json?"

        self.page = 1

        self.params = {
            "city": input("请输入需要抓取的城市:"),
            "needAddtionalResult": "false"
        }

        self.form_data = {
            "first": "false",
            "pn": self.page,
            "kd": input("请输入需要抓取的职位：")
        }

        self.item_list = []


    def send_request(self, url):
        print("[INFO]: 正在发送请求 {} {}".format(url, self.page))
        response = requests.post(url, params=self.params, data=self.form_data, headers=self.headers)
        return response


    def parse_page(self, response):

        python_obj = response.json()
        #pythob_obj = json.loads(response.content)

        result_list = jsonpath(python_obj, "$..result")[0]

        if not result_list:
            return True

        for result in result_list:
            item = {}
            # 职位创建时间
            item["createTime"] = result["createTime"]
            # 城市
            item["city"] = result["city"]
            # 职位名
            item["positionName"] = result["positionName"]
            # 薪资
            item["salary"] = result["salary"]
            # 公司规模
            item["companySize"] = result["companySize"]
            # 区域
            item["district"] = result["district"]
            # 公司名
            item["companyFullName"] = result["companyFullName"]

            self.item_list.append(item)


    def save_data(self):
        json.dump(self.item_list, open("lagou.json", "w"))


    def main(self):
        #while True:
        while self.page <= 10:
            response = self.send_request(self.post_url)
            if self.parse_page(response) == True:
                break
            self.page += 1

        self.save_data()


if __name__ == '__main__':
    spider = LagouSpider()
    spider.main()
