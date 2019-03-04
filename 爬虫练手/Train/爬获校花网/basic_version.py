import re 
import requests

response = requests.get('http://www.xiaohuar.com/hua/')

urls = re.findall(r'class="img".*?src="(.*?)"', response.text,re.S)
filenames = re.findall(r'class="img".*?alt="(.*?)"', response.text,re.S)
# print(filenames[0])
url = urls[0]
print(url)
filename = filenames[0] + '.jpg'

img_response = requests.get(url).content

with open('./img/' + filename, 'wb') as f:
	f.write(img_response)
