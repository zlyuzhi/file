import requests 
from lxml import etree
from urllib import request
import os,re
import threading
from queue import Queue
from timeit import timeit

"""
 main()
定义两个队列，和创建多线程
page_queue()：存放每一页的url
img_queue()：存放每一页里面所有的表情的url

Producer()
从page_queue()队列中去每一页的url，直到队列为空则break
用xpath提取出每一页的所有图片的url
把每个图片的url和名字存放到img_queue()队列里面

Consumer()
从img_queue()队列中取出图片的url和名字
下载保存
直到page_queue()和img_queue()两个队列都为空则break
"""
class Producer(threading.Thread):
	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }

	def __init__(self, page_queue, img_queue, *args, **kwargs):
		super(Producer, self).__init__(*args, **kwargs)
		self.page_queue = page_queue
		self.img_queue = img_queue

	def run(self):
		while True:
			if self.page_queue.empty():
				break
			url = self.page_queue.get()
			self.parse_page(url)

	def parse_page(self, url):
		response = requests.get(url, headers= self.headers)
		text = response.text
		html = etree.HTML(text)
		imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
		for img in imgs:
			# print(etree.tostring(img))
			#图片地址
			img_url = img.get('data-original')
			#图片名字
			alt = img.get('alt')
			#替换掉名字里面的特殊字符
			alt = re.sub(r'[\?？\.，。！!\*]','',alt)
			#获取图片的后缀名（.gif .jpg）
			suffix = os.path.splitext(img_url)[1]
			#保存的时候完整的图片名字
			filename = alt + suffix
			self.img_queue.put((img_url,filename))

class Consumer(threading.Thread):
	def __init__(self, page_queue, img_queue, *args, **kwargs):
		super(Consumer, self).__init__(*args,**kwargs)
		self.page_queue = page_queue
		self.img_queue = img_queue

	def run(self):
		while True:
			if self.img_queue.empty() and self.page_queue.empty():
				break
			img_url, filename = self.img_queue.get()
			request.urlretrieve(img_url,'./imags/'+filename)
			print("已下载一张图片")

def main():
	page_queue = Queue(1000)
	img_queue = Queue(10000)

	for x in range(1, 2):
		url = 'http://www.doutula.com/photo/list/?page=%d'%x
		page_queue.put(url)

	for x in range(5):
		t = Producer(page_queue, img_queue)
		t.run()
		t.start()

	for x in range(5):
		t = Consumer(page_queue, img_queue)
		t.run()
		t.start()

if __name__ == "__main__":
	# start = time()
	# main()
	# end = time()
	# run_time = end - start
	# print(run_time)
	t = timeit(main, number=1)
	print(t)