import json
import time
import threading
from queue import Queue

import requests
from lxml import etree


class ThreadCrawl(threading.Thread):
	def __init__(self, thread_name, page_queue, data_queue):
		# threading.Tread.__init__()
		super().__init__()

		self.thread_name = thread_name

		self.page_queue = page_queue

		self.data_queue = data_queue

		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

	def run(self):
		print ("启动" + self.thread_name)
		while not CRAWL_EXIT:
			try:
				# 取出一个数字，先进先出
				# 可选参数block，默认值为True
				#1. 如果对列为空，block为True的话，不会结束，会进入阻塞状态，直到队列有新的数据
				#2. 如果队列为空，block为False的话，就弹出一个Queue.empty()异常，
				page = self.page_queue.get(False)
				url = "http://www.qiushibaike.com/text/page/" + str(page) +"/"
				print(url)
				content = requests.get(url, headers=self.headers).text
				print(len(content))
				time.sleep(1)
				self.data_queue.put(content)
				
			except:
				pass
		print("结束" + self.thread_name)

class ThreadParse(threading.Thread):
	def __init__(self, thread_name, data_queue, filename, lock):
		super(ThreadParse, self).__init__()
		# 线程名
		self.thread_name = thread_name
		# 数据队列
		self.data_queue = data_queue
		# 保存解析后数据的文件名
		self.filename = filename
		# 锁
		self.lock = lock

	def run(self):
		print("启动" + self.thread_name)
		while not PARSE_EXIT:
			try:
				html = self.data_queue.get(False)
				self.parse(html)
			except:
				pass
		print("退出" + self.thread_name)

	def parse(self, html):
		# 解析为HTML DOM
		html = etree.HTML(html)

		node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

		for node in node_list:
			user_name = node.xpath('.//img/@alt')[0]
			image = node.xpath('.//img/@src')
			content = node.xpath('.//div[class="content"]/span')[0].text
			zan = node.xpath('.//i')[0].text
			comments = node.xpath('.//i')[1].text
			print(user_name)

			items = {
				"user_name" : user_name,
				"image": image,
				"centent": content,
				"zan": zan,
				"comments": comments
			}
			# with 后面有两个必须执行的操作：__enter__ 和 _exit__
			# 不管里面的操作结果如何，都会执行打开、关闭
			# 打开锁、处理内容、释放锁
			with self.lock:
				# 写入存储的解析后的数据
				self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")

CRAWL_EXIT = False
PARSE_EXIT = False

def main():
	page_queue = Queue(20)
	for i range(1, 2):
		page_queue.put(i)



	with lock:
		# 关闭文件
		filename.close()
	print("谢谢使用")


if __name__ == "__main__":
	main()