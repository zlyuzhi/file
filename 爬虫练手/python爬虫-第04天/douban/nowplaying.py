"""
常规操作；
注意点： #替换掉名字里面的特殊字符
		alt = re.sub(r'[\?？\.，。！!\*]','',alt)
		print(alt)
		# 获取图片的后缀名
		suffix = os.path.splitext(img_url)[1]
"""

import os,re
import requests
from lxml import etree
from urllib import request

class Spider(object):
	def __init__(self):
		self.url  = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
		self.headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
		"Referer":"https://movie.douban.com/",
		}

		self.page = 1
		self.params = {

		}
		self.form_data = {

		}
	def send_request(self, url):
		response = requests.get(url, headers=self.headers).content.decode()
		return response

	def parse_page(se, response):
		html = etree.HTML(response)
		data_list = html.xpath("//li[@class='poster']/a[@class='ticket-btn']/img")
		print(len(data_list))
		# data = etree.tostring(data_list[0])
		for data in data_list:
			img_url = data.xpath("@src")[0]
			alt = data.xpath("@alt")[0]
			# #替换掉名字里面的特殊字符
			alt = re.sub(r'[\?？\.，。！!\*]','',alt)
			print(alt)
			# 获取图片的后缀名
			suffix = os.path.splitext(img_url)[1]
			filename = alt + suffix
			request.urlretrieve(img_url,'./imags/'+filename)

	def save_data(self,):
		pass

	def main(self):
		response = self.send_request(self.url)
		self.parse_page(response)
		self.save_data()


if __name__ == "__main__":
	spider = Spider()
	spider.main()