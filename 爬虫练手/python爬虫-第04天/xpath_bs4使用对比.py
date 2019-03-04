import requests
from lxml import etree
from bs4 import BeautifulSoup
url = "https://hr.tencent.com/position.php?&start=10"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
html = requests.get(url, headers=headers).content

html_obj = etree.HTML(html)
html_obj.xpath("//tr[@class='even']")
html_obj.xpath("//tr[@class='odd']")
html_obj.xpath("//tr[@class='even'] | //tr[@class='odd']")

soup = BeautifulSoup(html, "lxml")
soup.find_all("tr")
# 找出所有的tr
len(soup.find_all("tr"))
# 找出所有指定属性的 tr
len(soup.find_all("tr", {"class" : "even"}))
len(soup.find_all("tr", {"class" : "odd"}))
len(soup.find_all("tr", {"class" : ["even", "odd"]}))

# 找出所有指定属性的 tr 和tmm，属性相同
len(soup.find_all(["tr", "tmm"], {"class" : ["even", "odd"]}))
# 根据属性查找所有指定的标签
len(soup.find_all(attrs={"class" : ["even", "odd"]}))
# 根据class属性超找所有指定的标签
len(soup.find_all(class_ = ["even", "odd"]))

# 找出所有class为 even 和 odd 的标签
len(soup.select(".even"))
len(soup.select(".even, .odd"))
len(soup.select("[class='even'], [class='odd']"))

%hist -f xpath_bs4使用对比.py
