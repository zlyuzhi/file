import requests
from lxml import etree
from urllib import request
import os, re

def parse_page(url):
	headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
	response = requests.get(url, headers=headers)
	text = response.content.decode('utf-8')
	html = etree.HTML(text)
	imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
	for img in imgs:
		# print(etree.tostring(imag))
		img_url = img.get('data-original')
		alt = img.get('alt')
		# #替换掉名字里面的特殊字符
		alt = re.sub(r'[\?？\.，。！!\*]','',alt)
		print(alt)
        # 获取图片的后缀名
		suffix = os.path.splitext(img_url)[1]
		filename = alt + suffix
		request.urlretrieve(img_url,'./imags/'+filename)

url = 'http://www.doutula.com/photo/list/?page=1'
parse_page(url)
