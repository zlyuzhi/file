#coding:utf-8

import urllib
import urllib2


class TiebaSpider(object):
    def __init__(self):
        # 固定的url地址
        self.base_url = "https://tieba.baidu.com/f?"
        # 请求报头
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 贴吧名
        self.tieba_name = raw_input("请输入需要抓取的贴吧:")
        # 起始页
        self.begin_page = int(raw_input("请输入抓取的起始页："))
        # 结束页
        self.end_page = int(raw_input("请输入抓取的结束页："))


    def send_request(self, url):
        """
            接收url地址，发送请求，返回响应
        """
        request = urllib2.Request(url, headers = self.headers)

        print("[INFO] : 正在发送请求 {}..".format(url))
        response = urllib2.urlopen(request, timeout=3)

        return response


    def save_page(self, response, file_name):
        """
            接收响应，保存数据
        """
        print("[INFO] : 正在保存数据 {}..".format(file_name))

        with open(file_name, "w") as f:
            f.write(response.read())


    def main(self):
        """
            爬虫调度中心，控制功能调用
        """
        for page in range(self.begin_page, self.end_page + 1):
            # 根据page值 计算pn值
            pn = (page - 1) * 50

            # 构建查询字符串
            query_dict = {"kw" : self.tieba_name, "pn" : pn}
            query_str = urllib.urlencode(query_dict)

            # 拼接为完整的url地址
            full_url = self.base_url + query_str
            # 文件名
            file_name = self.tieba_name + str(page) + ".html"

            try:
                # 发送请求获取响应
                response = self.send_request(full_url)
                # 保存响应内容到文件中
                self.save_page(response, file_name)
            except Exception as e:
                print("[ERROR] : 页面抓取失败 {}".format(full_url))
                print(e)


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.main()

