import requests
from bs4 import BeautifulSoup
url = "https://hr.tencent.com/position.php?&start=10"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "lxml")

node_list = soup.find_all("tr", {"class" : ["even", "odd"]})

node_list[0].td
node_list[0].find_all("td")
node_list[0].select("td")

node_list[0].select("td")[0]
node_list[0].select("td")[0].a

node_list[0].select("td")[0].a.string
node_list[0].select("td")[0].a.text
node_list[0].select("td")[0].a.get_text()

node_list[0].select("td")[0].a.get("href")
node_list[0].select("td")[0].a.attrs
node_list[0].select("td")[0].a.attrs["href"]

%hist -f bs4提取文本和属性值.py
