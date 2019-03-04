import requests
from lxml import etree
from requests.exceptions import RequestsException

class Spider(object):
	def __init__(self):
		self.url  = ''
		self.headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
		
		}
		# self.page = 1
		# self.params = {

		# }
		# self.form_data = {

		# }
	def send_request(self, url):
		try:
			response = requests.get(url, headers=self.headers).content.decode()
			if response.status_code == 200:
				return response
			return None
		except RequestsException:
			print('爬取失败')

	def parse_page(self, response):
		html = etree.HTML(response)
		data_list = html.xpath("")

	def save_data(self):
		pass

	def main(self):
		response = self.send_request(self.url)
		self.parse_page(response)
		self.save_data()


if __name__ == "__main__":
	spider = Spider()
	spider.main()