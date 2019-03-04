import requests
url = 'https://www.aliyun.com/price/detail/ecsnew#/?_k=jxd17m'
# url = 'https://www.baidu.com'
# proxies = {'https': '101.236.54.97:8866'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',}
res = requests.get(url, headers=headers)
content = res.content.decode()
print(content)