#coding:utf-8

import requests
import re


class NeihanSpider(object):
    def __init__(self):
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 固定url部分
        self.base_url = "https://www.neihan8.com/article/list_5_"
        # 自增页码
        self.page = 1

        # 匹配网页中所有段子内容
        # 启用DOTALL模式，让 . 也可以匹配换行符
        self.pattern_page = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)

        # 匹配网页中无用字符：
        # \s 表示空白字符（如\n \r 空格等）
        # <.*?> 表示标签 （如 <p> <br>等）
        # &.*?; 表示HTML实体字符（如 &nbsp;等）
        # 　 或 u"\u3000".encode("utf-8") 表示中文全角空格，无法被\s匹配
        #self.pattern_content = re.compile(r"\s|<.*?>|&.*?;|　")
        self.pattern_content = re.compile(r"\s|<.*?>|&.*?;|" + u"\u3000".encode("utf-8"))


    def send_request(self, url):
        """
            接收url地址并发送请求，返回响应
        """
        response = requests.get(url, headers=self.headers)
        return response


    def parse_response(self, response):
        """
            接收响应，提取数据
        """
        # 将网页转码为 utf-8 字符串（原始编码为gbk)
        html = response.content.decode("gbk").encode("utf-8")
        # 匹配网页中的每条段子，并返回所有匹配结果对列表
        content_list = self.pattern_page.findall(html)

        return content_list


    def save_content(self, content_list):

        with open("duanzi.txt", "a") as f:
            f.write("第{}页:\n".format(self.page))
            for content in content_list:
                # 对每条段子进行数据清洗，去除无用字符
                result = self.pattern_content.sub("", content)
                f.write(result)
                f.write("\n")

            f.write("\n")


    def main(self):
        while True:
            if input("按下回车继续抓取（输入q则退出）：").lower() == 'q':
                break

            # 构建完整的url地址
            full_url = self.base_url + str(self.page) + ".html"

            try:
                # 发送请求，返回响应
                response = self.send_request(full_url)
                # 解析响应，返回解析结果
                content_list = self.parse_response(response)
                # 保存解析结果
                self.save_content(content_list)
            except Exception as e:
                print("[ERROR]: 数据抓取失败 {}".format(full_url))
                print(e)

            self.page += 1

        print("[INFO]: 谢谢使用！")

if __name__ == '__main__':
    spider = NeihanSpider()
    spider.main()

