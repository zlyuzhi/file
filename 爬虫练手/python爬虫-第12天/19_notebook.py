第一天：

数据工程：
  数据采集 和 数据存储（爬虫系统）
  数据计算、分析 和 数据可视化（数据分析）
  数据建模 和 数据训练（数据挖掘、机器学习）

1. 什么是爬虫？
  抓取网页数据的程序。

2. 爬虫是怎么抓取网页的数据？

  网页三个特征：
  -1. 每个网页都有自己的URL（统一资源定位符）进行互联网上定位
  -2. 网页都使用HTML（超文本标记语言）来描述页面信息
  -3. 网页都使用 HTTP、HTTPS（超文本传输协议）来传输HTML

  爬虫的设计流程：
  -1. 客户端通过 HTTP协议 发送网页的URL地址 请求给服务器端
  -2. 服务器端返回 HTTP 响应给客户端，客户端获取响应中的 HTML内容（json、JavaScript、mp3、avi、jpg）
  -3. 通过相关的 HTML 解析工具，提取网页里的数据：
    -a. 如果是需要保存的目标数据，则根据业务需求进行保存（txt、json、csv、mongodb、redis、mysql）
    -b. 如果是需要继续抓取的新的URL地址，则从第二步继续执行
  -4. 当所有的 URL 地址全部抓取完毕，程序结束。

3. 爬虫抓下来的数据能干嘛？
  1. 爬虫属于数据工程的第一环，数据可以用于数据分析、数据计算、数据挖掘、机器学习、模型训练
  2. 爬虫各个网站的数据，整理后用于自己的网站，提供网站流量
  3. 数据也可以单独卖钱
  4. 抓取友商的数据，及时调整自己的产品信息，提供产品竞争力
  5. PPT创业，吹牛融资，要有数据支持。


4. Java、Python、PHP、CC++

  PHP 并发能力相对较弱，不适合大规模数据抓取
  Java 开发成本和重构成本相对较高，代码量大
  CC++ 学习成本高
  Python 语法优美，代码简介，大量的HTTP请求处理库和HTML解析库，
      强大的爬虫框架 Scrapy，以及高效成熟的分布式组件scrapy-redis

  Python 是动态、强类型、解释型语言。

  动态：数据类型在执行时确定
  静态：数据类型在执行前确定

  强类型：不同类型互相运算时，会报错
  弱类型：不同类型互相运算时，不会错

  解释型：按行执行，每次执行都重新解释一遍代码
  编译型：先通过编译器生成可执行文件，之后运行可执行文件即可

  解释型语言的执行效率低下问题，可以被机器性能所弥补。


5. 课程介绍：

  1. Python基本语法、HTML和JavaScript

  2. HTML页面的抓取：
      urllib、urllib2、requests ：通过 模拟浏览器 发送HTTP请求，获取服务器的响应

  3. HTML页面的解析：
      re、lxml/xpath、bs4/BeautifulSoup、pyquery、jsonpath ： 通过特定语法，匹配网页符合规则的数据

      字符串、列表、字典

  4. 对解析结果的存储 MongoDB：
      txt、json、csv、mongodb、redis、mysql

  5. 动态HTML处理、验证码处理
      Selenium+PhantomJS/Chrome：在爬虫程序中调用浏览器渲染页面，获取网页内容（直接处理js加密、ajax）
      Tesseract OCR（光学字符识别系统）：将图片验证码“读取”出来，返回字符串

      函数 - 类 - 模块 - 包/库 - 框架

  6. Scrapy框架
      高性能高定制性的爬虫框架，提供了请求发送，响应解析，数据存储，请求去重等功能，使用了twisted异步网络框架处理请求并发。

  7. scrapy-redis分布式组件
      分布式爬虫：在不同的网络环境和硬件环境下，共享请求队列。

      scrapy原本不支持分布式（数据在内存保存不能共享），所以 scrapy-redis 的解决方案就将所有请求保存在同一个redis数据库里，让所有的爬虫端访问。

      一套以redis数据库为核心的组件，用来替换scrapy部分组件，用于支持分布式。

  8. 定制化爬虫框架

    爬虫的最高境界：
    1. 做一个通用的搜索引擎（Google、Baidu）：硬件支持、资金支持、政策支持
    2. 根据业务需求，编写一个爬虫框架


  9. 爬虫 - 反爬虫 - 反反爬虫 之间的斗争

    网站为什么要反爬？
    1. 过高的爬虫访问，会提高服务器负载，反爬可以保护服务器
    2. 保护数据，提供网站竞争力
        机器成本 + 人力成本 == 数据价值
    3. 面子问题

    毛主席说过：战略上藐视，战术上重视。

    只要是真实用户可访问的网页，爬虫一定有办法将数据抓下来。








一、什么是字符编码？
    计算机里的所有数据，本质都是二进制

    二进制 0b01100001  十进制 97  通过 ASCII编码表 对应字符 'a'

    计算机是美国人发明，一开始制定字符编码只考虑了英文 ASCII编码表（包含英文、数字和常用字符）， 0~127

    后来计算机开始普及全球，各个国家的语言不一样，ASCII编码不满足各国字符需求，于是各国开始制定自己的编码表。(注意，都是在ASCII编码基础上扩展，所有任何编码的前 127 都是一样的)
    简体中文： gb2312、gbk、gb18030, cp936 ,code page 936，一个汉字2个字节
    繁体中文： Big5
    日文：Shift-jis

    世界编码不统一，文化交流很费劲，会出现乱码。（乱码是指，按当前的编码表 来 显示其他编码的文字）。

    诞生了 Unicode编码，包含了世界上所有国家的字符，对编码进行了大一统。 每个字符占用 3~6 个字节，浪费空间。

    诞生了 utf-8 可变长的Unicode，一个汉字占3个字节，一个字母占1个字节，大大了减少了空间占用。

    utf-8是目前世界上应用最广泛的字符编码，所有的Linux操作系统终端编码都是utf-8，90%以上的网页都使用utf-8


爬虫程序处理编码的场景：
1. 发送请求获取网页内容（不同的网页编码可能不一样）
2. 程序处理时产生的字符串（可能会有不同编码）
3. 保存结果需要统一编码（写入保存时候的编码）


二、Python2和Python3的 字符编码 和 字符类型

Python3:
    Unicode字符串 str 类型
    非Unicode字符串 bytes 类型

Python2：
    Unicode字符串 unicode 类型
    非Unicode字符串 str 类型



三、编码的转换
    任何语言、任何平台、任何编码的字符串，都可以和Unicode互相转换。

    例 ： utf8_str  -> gbk_str

    # 非Unicode字符串，可以通过decode解码为Unicode字符串
    unicode_str = utf8_str.decode("utf-8")
    # Unicode字符串, 可以通过 encode 编码为其他编码
    gbk_str = unicode_str.encode("gbk")

    反之： gbk_str -> utf8_str
    unicode_str = gbk_str.decode("gbk")
    utf8_str = unicode_str.encode("utf-8")

    UnicodeDecodeError、UnicodeEncodeError


四、终端创建字符串的编码

    在解释器终端创建的字符串

    Python2：根据操作系统决定
            Linux 为 utf-8、 简体中文Windows 为 gbk。注意，如果是iPython创建的，都是 utf-8

    Python3： Unicode 编码



五、文件编码
    写入字符串到文件中，文件创建成功，则文件编码等同于写入的字符串编码。

    如果写入了其他编码的字符串，则文件编码被修改，原来的内容会变成"乱码"。



六、处理字符串写入文件时候的编码。

    Python不能直接写 Unicode字符串到文件中，必须写入 非Unicode

    1. 手动转码处理

        Python3:
            # w 必须写 Unicode， wb 写非Unicode（gbk、utf-8、jpg、mp4)
            with open("xxx.txt", "wb") as f:
                f.write(unicode_str.encode("utf-8"))

        Python2:
            # w 写字符串， wb 写非字符串
            with open("xxx.txt", "w") as f:
                f.write(unicode_str.encode("utf-8"))


    2. 通过 open()方法的 encoding 参数

        Python3:
            with open("xxx.txt", "w", encoding="utf-8") as f:
                f.write(unicode_str)

        Python2：
            Python2的 open() 没有 encoding，但是可以通过 codecs 模块解决

            import codecs
            with codecs.open("xxx.txt", "w", encoding="utf-8") as f:
                f.write(unicode_str)


    3. 如果强行写入Unicode字符串，且并没有通过 1 和 2 处理，则Python解释器编码尝试转码再写入。

         with open("xxx.txt", "w") as f:
             f.write(unicode_str)

        Python2 默认解释器编码是 ascii，在处理中文则报错 UnicodeEncodeError 无法按 ASCII编码处理中文字符串，

            解决方案，将Python2 解释器编码修改为 utf-8

            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")


        Python3 默认解释器编码是 utf-8，不会出现任何错误


七、代码文件头部编码声明
    Python2 默认代码文件编码声明是 ascii，所以代码中有中文部分会报错，
    解决方案，在代码第一行添加

    #coding:utf-8

    Python3 默认代码文件编码声明是 utf-8，所以不需要修改。



八、urlencode编码

import urllib
qeryt_str = urllib.urlencode({"wd" : "你好"})


https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD&pn=40



第二天：


https://tieba.baidu.com/f?

kw 表示贴吧名
pn 表示页码

page = 1  pn = 0
page = 2  pn = 50
page = 3  pn = 100

pn = (page - 1) * 50




静态页面：数据保存在网页的HTML中
动态页面：数据不直接保存在HTML中，而是服务器后台单独传输数据，再渲染到页面中。
  动态页面获取数据，必须抓包，找出浏览器和服务器之间传递的数据（json、js、xml）


GET： 可能会有查询字符串，但是一定没有表单数据（查询字符串会显示在url后面）
POST： 可能会有查询字符串，但是一定有表单数据（表单数据保存在请求体里发送）

"https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

start=0&limit=50



post_url = "https://fanyi.qq.com/api/translate"




匹配："""  ^(.*?):\s(.*?)$  """
替换：""" "\1" : "\2", """

Sublime Text： 选中部分向下多选， ctrl + d

source: auto
target: en
sourceText: 象宝宝
qtv: e8fbdcdd4cdfc789
qtk: hZ0SKxtrrKHrmuPTyRiOGSmx0YlAWAMxomxdEG5i54X+BhnrpM+zZJtSxxWNSHzkXBMCXQWgQhj7r6uthSbnndMokR1P/H/H+nPPNnO90Veu/7v46adMihj380KSpqXENEqkmSplLo3CApiarKroNQ==
sessionUuid: translate_uuid 1542009952608
                              UNIX时间戳： 1970.1.1 到现在的秒数

source: auto
target: en
sourceText: 大象
qtv: e8fbdcdd4cdfc789
qtk: hZ0SKxtrrKHrmuPTyRiOGSmx0YlAWAMxomxdEG5i54X+BhnrpM+zZJtSxxWNSHzkXBMCXQWgQhj7r6uthSbnndMokR1P/H/H+nPPNnO90Veu/7v46adMihj380KSpqXENEqkmSplLo3CApiarKroNQ==
sessionUuid: translate_uuid 1542010053705


UNIX时间戳： 10位 / 13位 纯数字，今年 15开头，明年16开头
md5 sha1 不可逆加密：生成的结果是 十六进制数形式的字符串，小写字母（最大是f）+数据
base64 加密： 大小写字母混合+数字，且后面一两位 是 =

i: 大象宝宝
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 1542012823009
sign: eb2283a7c57a49169131f7920a1297c9
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
typoResult: false


i: 宝宝
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 1542013054428
sign: a6bf6c4faa0b09fa3504900bc1839f85
      a6bf6c4faa0b09fa3504900bc1839f85

doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
typoResult: false

import hashlib

hashlib.md5("fanyideskweb" + "宝宝" + "1542013054428" + "sr_3(QOHT)L2dx#uuGR@r").hexdigest()


salt = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
salt = str(int(time.time() * 1000) + random.randint(0, 10))

sign = md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")

e 是需要翻译的文本
t 是 salt


Python自带的： "/usr/lib/python2.7/"
第三方安装的： "/usr/local/lib/python2.7/"



10% 有反爬 -> 90%只做到封禁IP

1. 请求报头
2. 代理IP
3. 数据加密
4. 页面重构
5. 验证码

网站反爬不会太过严格，考虑是否会误伤真实用户。


代理的API： "http://kps.kdlapi.com/api/getkps/?orderid=914194268627142&num=1&pt=1&sep=1"

proxy = {
    "http" : "http://maozhaojun:ntkn0npx@39.106.10.232:16818"}



Cookie的两种用法：
1. （最常用最简单）直接手动登录网站并保存cookie，用于程序的请求报头中
2. （不常用很复杂）模拟登录：
    -1. 先分析登录页面，抓包获取需要的登录参数
    -2. 发送登录页面的get请求，提取登录参数
    -3. 附带登录参数 和 账户密码，发送post登录请求，如果登录成功则记录cookie
    -4. 附带这个登录后的cookie，发送其他需要登录才能访问的页面

post_url = "http://www.renren.com/PLogin.do"

email
password



response = urllib2.urlopen()
response.read()# 获取网页原始编码字符串，也可以获取图片音视频等字节数据

import requests

response = requests.get()
response.content # 获取网页原始编码字符串，也可以获取图片音视频等字节数据
response.text # 获取网页Unicode编码字符串

response.encoding = "utf-8" # 手动指定网页的编码，如果不指定则靠猜
response.text # 根据encoding来解码，获取网页Unicode编码字符串


# 不会记录cookie
requests.get()
requests.post()

# 记录cookie
ssion = requests.session()
ssion.get()
ssion.post()
ssion.get()



第三天：

urllib2 和 Requests

1. Get请求:
query_str = urllib.urlencode({})
request = urllib2.Request(url + query_str, headers)
response = urllib2.urlopen(request)
response.read() # 网页原始编码字符串，还可以图片音视频等字节流数据


response = requests.get(url, params={}, headers)
response.content # 网页原始编码字符串，还可以图片音视频等字节流数据
response.text # 网页Unicode编码字符串


2. Post请求（必须抓包获取表单数据）：

request = urllib2.Reuqest(url + query_str, data, headers)
urllib2.urlopen(request)


requests.post(url, params, data, headers)


3. 代理ip的使用

proxy = {"http" : "http://username:passwd@ip:port"}

proxy_handler = urllib2.ProxyHandler(proxy)
opener = urllib2.build_opener(proxy_handler)
opener.open(request)


requests.get(url, headers, proxies=proxy)


4. Cookie的两种用法:
  -1. 放在请求报头里
  -2. 通过请求生成cookie并保存，并传递给后续的请求

cookie_jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_handler)
opener.open()
opener.open()


ssion = requests.session()
ssion.get()
ssion.post()




re.findall()

pattern = re.compile()
pattern.findall()



"https://www.neihan8.com/article/list_5_" + page + ".html"   page += 1

'<div class="f18 mb20">(.*?)</div>'

l = ['aaa', 'bbb', 'ccc']


列表 转 字符串  : s =  " ".join(l)
字符串 转 列表  :  l = s.split()

XPath
1. 永远返回一个列表：有数据的列表 或 空列表

2. XPath匹配时，下标从 1 开始

3. XPath取值的 目标值 两种：
  -1. 指定标签的文本内容  （如取文本）
  -2. 指定标签的指定属性值 （如取链接）

  XPath取出的字符串数据，都是Unicode编码字符串。

4. 如果取值的目标值很多，可以先获取所有结点列表，再迭代取值：
# 获取结点列表
node_list = "//div[@class='f18 mb20']"

for node in node_list:
  item = {}
  item['text'] = " ".join(ode.xpath("./text()"))
  item['a_text'] = node.xpath("./a/text()")[0]
  item['link'] = node.xpath("./a/@href")[0]

html = response.read()
html = response.content

# 导入lxml类库里的 etree模块
from lxml import etree
# 通过 etree模块的 HTML类 获取 HTML DOM对象
html_obj = etree.HTML(html)
# html_obj = etree.parse("./baidu.html")
# html = etree.tostring(html_obj)

node_list = html_obj.xpath("//div[@class='f18 mb20']/a/@href")





获取每个帖子的链接： "http://tieba.baidu.com" + "//a[@class='j_th_tit']/@href"

获取每个图片的链接 ： "//img[@class='BDE_Image']/@src"


我亦无他，唯手熟尔。



第四天：



BeautifulSoup4 的常用匹配方法：
1. find() : 匹配网页中第一个符合规则的结果，并返回该结果
2. find_all() ：匹配网页中所有符合规则的结果，并返回结果列表
    find() 和 find_all() 语法相同
3. select() ： 匹配网页中所有符合规则的结果，并返回结果列表（使用CSS选择器用法）



url = "https://hr.tencent.com/position.php?&start=0" += 10


item_list = []
node_list = soup.find_all("tr", {"class" : ["even", "odd"]})

for node in node_list:
    item = {}
    item['position_name'] = node.find_all("td")[0].a.text
    item['position_link'] = node.find_all("td")[0].a.get("href")
    item['position_type'] = node.find_all("td")[1].text
    item['people_number'] = node.find_all("td")[2].text
    item['work_location'] = node.find_all("td")[3].text
    item['publish_times'] = node.find_all("td")[4].text
    item_list.append(item)



多页抓取的停止条件设定：

1. 通过提取下一页链接，并判断是否是最后一页方式

2. 通过提取总页数，再用列表推导式的方式获取所有url地址（支持并发处理）
    url_list = ["https://hr.tencent.com/position.php?&start=" + str(page * 10) for page in range(0, 281)]

3. 根据响应状态码（不是200就有问题） / 响应内容（没有需要的数据）
        if not node_list:
            return



通过xpath和bs4提取的字符串数据，都是Unicode编码



Json模块的使用注意：

1. 通过json模块的 dumps或dump 方法，将Python数据转为json字符串并写入文件，默认按Unicode样式写入，文件编码为 ascii 。
    如果希望按utf-8编码写入，可以添加 ensure_ascii=False 参数，则表示不按Unicode样式写入，按解释器编码 转码再写入：

    json_str = json.dumps(item_list, ensure_ascii=False)
    with open("tencent_utf8.json", "w") as f:
        f.write(json_str)

    json.dump(item_list, open("tencent_utf8.json", "w"), ensure_ascii=False)

    Python3的解释器编码，默认为utf-8 可以正常写入数据；
    Python2的解释器编码，默认为 ascii，如果数据内有中文则报出 UnicodeEncodeError,解决方案是修改解释器编码 为 utf-8
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")


2. 将Python数据 通过json模块按 默认方式写入，文件里的 Unicode 没有前缀 u,
    但是通过 json.load() json.loads()读入，即可复原为 Unicode


3. 将 类Unicode的普通字符串，转为 真正的 Unicode字符串
# 类似Unicode的普通字符串
s = '\u6df1\u5733'
# 解码为真正的Unicode
s.decode("unicode-escape")
u'\u6df1\u5733'



post_url = "https://www.lagou.com/jobs/positionAjax.json?"

params = {"city": "深圳",
"needAddtionalResult": "false"}

form_data = {"first": "false",
"pn": "2",
"kd": "python"}



第五天：




SQL：（MySQL、Oracle、SQL Server、DB2）
1. 高度事务性的场景，银行、会计、贸易、库管，需要大量原子性操作
2. 数据存储要求有规范的多表结构设计，预定义明确的字段
3. 数据价值高，对安全和稳定性要求高
4. 需要持久化存储的 "冷数据"（不需要经常读写的数据）
5. 需要通过SQL语句支持的存储场景


NoSQL：
    Redis   key:value(string、list、hash、set、zset)
    MongoDB  {key1 : value1, key2 : value2}, {key1 : value1}
1. 高度伸缩性场景，更容易扩展，支持集群
2. 灵活的数据结构，不需要事先设计数据库数据表字段，即用即存，社交网络、热点资讯
3. 处理 "热数据"（需要经常读写的数据），NoSQL大部分操作都是和内存交互，读写效率极高
4. 不需要SQL语句支持，学习成本低



32bit:  内存最大的寻址范围 2^32



MySQL 3306
Redis 6379
MongoDB 27017

127.0.0.1

MongoDB 服务和客户端 命令：

1. 开启数据库服务： sudo mongod
2. 开始shell客户端： mongo
3. 关闭 shell客户端 和 数据库服务， ctrl + c
4. 在admin数据库下，通过 db.shutdownServer() 来关闭服务


MongoDB数据库操作的常用命令：

1. 表示当前所在的数据库
> db

2. 查看所有的数据库
> show dbs

3. 切换到指定数据库
> use mydb

4. 查看当前数据库下的所有集合（相当于SQL的表）
> show collections

5. 查看当前数据库下 指定集合 的所有文档（相当于 每一条数据）
> db.mycollection.find()

6. 删除当前数据库的 指定集合
> db.mycollection.drop()

7. 删库
> db.dropDatabase()


不要把 生产环境 当成 测试环境。


MongoDB 的 用户权限：
1. 第一次进入到MongoDB没有用户，所以是root权限，
    需要先创建一个有root权限的用户:
    > use admin
    > db.createUser()

    在使用这个用户创建其他用户
    > db.auth()

2. 第二次开启MongoDB服务，要通过 --auth 启动用户权限模式，才可以让用户权限生效。
    > use admin
    > db.auth()





------------------  MongoDB 增加数据 ： insert

1. insert() 接收一个文档 参数

> db.stu.insert({ "_id" : 1, "name" : "诸葛亮", "age" : 40, "hometown" : "蜀" })

2. 构建空文档，添加字段，再写入

> data = {}
> data._id = 2
> data.name = "刘备"
> data.age = 48
> data.hometown = "蜀"

db.stu.insert(data)



------------------  MongoDB 删除数据 ： remove

1. 删除所有符合条件的文档,也可以同时指定多个条件
> db.stu.remove({"age" : 18})
> db.stu.remove({"age" : 18, "hometown" : "蜀"})

2. 只删除第一个符合条件的文档，通过添加第二个参数 {justOne : true}

> db.stu.remove({"age" : 18}, {justOne : true})

3. 不添加任何条件，则删除全部文档
> db.stu.remove()
> db.stu.drop()


------------------  MongoDB 修改数据 ： update

update() 至少需要两个参数，第一个参数为匹配条件，第二个参数为修改内容（可添加第三个参数表示是否全部匹配）

1.  将第一个符合条件的文档，替换为 第二个参数对应的文档（整个文档替换）
# 将第一个 age 为48的文档，替换为 {age : 49}， 但是 _id 保持不变
> db.stu.update({age : 48}, {age : 49})


2. 如果只修改特定字段，通过 $set 修饰符处理          （局部文档修改）
# 将第一个age为48的文档，修改age为49，其他字段保持不变
> db.stu.update({age : 48}, {$set : {age : 49}})
# 将第一个age为48的文档，修改age为49，并添加gender字段，其他字段保持不变
> db.stu.update({age : 48}, {$set : {age : 49, gender : true}})


3. 默认只处理第一条符合条件的文档，通过第三个参数 {multi : true} 表示全部处理 （修改所有文档）
# 将所有age为48的文档，修改age为49，其他字典不变
> db.stu.update({age : 48}, {$set : {age : 49}}, {multi : true})



------------------  MongoDB 新增+修改数据 ： save

save() 需要一个文档参数，根据文档的 _id 来处理，

1. 如果_id 存在，则修改数据，
> db.stu.save({_id : 1, name : "马超", age : 36, hometown : "蜀"})

2. 如果_id 不存在则新增
db.stu.save({_id : 5, name : "黄忠", age : 56, hometown : "蜀"})


insert() 如果_id存在则报错， save则修改数据
update() 修改数据可以指定字段修改，save则全部替换。



# pip install pymongo
import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
client.test.stu.insert({})
client.test.stu.insert([{}, {}, {}])
client.test.stu.find({})



------------------  MongoDB 查询数据 ： find()

1. find()  和  findOne()
find() 查询所有符合条件的文档
findOne() 查询第一个符合条件的文档

> db.stu.find({age : 18, hometown : "桃花岛"})
> db.stu.findOne({age : 18})




2. 比较运算符（通常用于比较数据，如果是字符串则比较字节码）

默认是 等于
$gt  大于
$gte 大于等于
$lt  小于
$lte 小于等于
$ne  不等于

> db.stu.find({age : 18})
> db.stu.find({age : {$gt : 18}})



3. 逻辑运算符（用于表示多个 独立条件的逻辑关系）

$and  和 $or  用来修饰多个条件的 数组

> db.stu.find({age : 18, hometown : "桃花岛"})

> db.stu.find( {$or : [{age : 18}, {hometown : "桃花岛"}]})

> db.stu.find( {$or : [ {$and : [{age : 18}, {hometown : "桃花岛"}]}, {gender : true}]})


4. 范围运算符

$in 在
$nin 不在

# 查找age 不是 16 18 20 的文档信息
db.stu.find({age : {$nin : [16, 18, 20]}})

# 查找age 是 16 18 20 ， 同时 hometown 是 蒙古 或 大理
db.stu.find({age : {$in : [16, 18, 20]}, hometown : {$in : ["蒙古", "大理"]}})


5. 正则表达式

# 按正则表达式匹配文档， / / 内写的正则表达式匹配文本
db.stu.find({name : /^黄/})

# 通过 $regex修饰 启动正则匹配文本
db.stu.find({name : {$regex : "^黄"}})

# 通过 $options 启动正则修饰 ,如 $i 表示 忽略英文大小写
db.stu.find({name : {$regex : "^Big", $options : "$i"}})



6. 自定义函数查询  $where (了解)
db.stu.find({$where : function() { return this.age != 20 }




----------- 对find() 查询结果的处理：

1. limit() 和 skip()

limit() 表示开始显示多少个
> db.stu.find().limit(3)

skip() 表示跳过多少个开始显示
> db.stu.find().skip(3)

如果 limit()和 skip()组合使用，执行结果一定是先 执行 skip() 再执行 limit()
> db.stu.find().skip(3).limit(3)


2. 投影显示
当find() 添加第二个参数，表示启用投影，可以指定字段显示

-1. 通过 1 和 true 指定显示字段，默认其他字段不显示
> db.stu.find({}, {name : 1, age : true})

-2. 通过 0 和 false 指定不显示字段，默认其他字段显示
> db.stu.find({}, {name : 0, hometown: false})

默认情况下，_id 是一定显示的，除非手动指定不显示
> db.stu.find({}, {name : 0, hometown: false, _id : 0})


3. sort() 排序

sort() 指定任意字段排序，1 为升序， -1 为降序，通常对数字排序，如果是字符串则按首字母的ascii值排序

-1. 单个排序
# 按年龄进行升序排序
> db.stu.find().sort({age : 1})

-2 多个排序：先执行第一个排序，如果出现重复值，再按第二个排序处理
# 先按age进行升序排序，如果有age相同的文档，再按 gender 降序排序
> db.stu.find().sort({age : 1, gender : -1})


4. count() 统计个数

-1. 在find()后添加 count() 统计文档个数
> db.stu.find({age : {$gte : 18}}).count()

-2. 代替find() 直接统计个数
> db.stu.count()
> db.stu.count({age : {$gte : 18}})


5. distinct() 去重显示

-1. 直接显示指定字段去重后的 数组
> db.stu.distinct("hometown")


-2. 配合查询条件，显示符合条件的文档中 指定字段的值
> db.stu.distinct("hometown", {age : {$gte : 18}})



数据分析：统计+概率

----------- MongoDB 的聚合运算

aggregate([ {$match}, {$group}, {}   ])


1. $group 分组统计

对所有文档按 gender进行分组，再分别统计每组 age 的总和

-1 $sum 求和统计计算


-2 $sum : 1 统计个数


-3 $avg : 统计平均数


-4 $max 和 $min  求最大值和最小值


-5 $first 和 $last 求第一个和最后一个



db.stu.aggregate([
    {
        $group : {
            # 表示分组依据
            _id : "$gender",
            # 统计 文档个数
            count : {$sum : 1},
            # 统计 age 总和
            sum_age : {$sum : "$age"},
            # 统计 age 平均数
            avg_age : {$avg : "$age"},
            # 统计 age 最大值
            max_age : {$max : "$age"},
            # 统计 age 最小值
            min_age : {$min : "$age"},
            # 统计 第一个 name
            first_name : {$first : "$name"},
            # 统计 最后一个 name
            last_name : {$last : "$name"},
            # 统计所有hometown 并保存在数组中
            all_hometown : {$push : "$hometown"}
        }
    },
    {

    }
])


2. $match 文档条件匹配（通过配合$group做预处理，将符合条件的文档再通过group分组统计）

db.stu.aggregate([
    # 先找出所有 hometown 不为 汉 文档
    {$match : {"hometown" : {$nin : ["汉"]}}},
    # 在match匹配结果里，按 gender进行分组，再统计所有文档的 name
    {$group : {_id : "$gender", all_name : {$push : "$name"}}}
])

3. $project 投影显示


db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}}, {$project : {_id : 0, max_age : 1}}])




4. $sort 排序处理

db.stu.aggregate([
    {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}},
    {$sort : {min_age : 1, max_age : -1}}
])



5. $limit 和 $skip
> db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}}, {$sort : {min_age : 1, max_age : -1}}, {$limit : 3}, {$skip : 2}])
{ "_id" : "蒙古", "max_age" : 20, "min_age" : 18 }
>
> db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}}, {$sort : {min_age : 1, max_age : -1}}, {$skip : 2}, {$limit : 3}])


# Python代码用法：
stu.aggregate([ {"$group" : {"_id" : "$hometown", "max_age" : {"$max" : "$age"}, "min_age" : {"$min" : "$age"}}}, {"$sort" : {"min_age" : 1, "max_age" : -1}}, {"$skip" : 2}, {"$limit" : 3}])

6. $unwind
db.stu.aggregate([ {$group : {_id : "$hometown", all_name : {$push : "$name"}}}, {$unwind : "$all_name"} ])




----------  MongoDB的索引操作 （索引是在集合为单位）

for(i=0;i<100000;i++)
{
    db.data.insert({_id : i, name : "name"+i, age : i+10})
}

0. 查看find() 执行状态

> db.data.find({_id : 10240}).explain("executionStats")


1. 查看索引，每个索引对应 一个name 索引名
> db.data.getIndexes()


2. 创建索引
> db.data.ensureIndex({name : 1})


3. 删除索引 （根据索引名删除，通过getIndexes()查看）
> db.data.dropIndex("name_1")




------------  MongoDB 的集合数据 导出 和 导入 （以集合为单位）


1. 将指定数据库 指定集合 的数据 导出为 json 或 csv
# 默认输出为json
sudo mongoexport -d test -c stu -o ./stu.json
# 通过--type指定导出为csv文件，并通过 -f 添加字段
sudo mongoexport -d test -c stu -o ./stu.csv --type csv -f "_id,name,age,hometown,gender"


2. 将json文件导入到 mongodb 指定的数据库 指定的集合里
sudo mongoimport -d test -c stu --file ./stu.json


--------------  MongoDB 数据库的 备份和恢复（以数据库为单位）


1. 数据库的备份

# 将 -h 指定的MongoDB服务器 的 -d 指定的数据库，备份到-o指定的目录中
$ sudo mongodump -h 192.168.37.80  -d test -o ./mongo_data/

2. 数据库的恢复
# 将 --dir 指定的数据库目录里的文件，恢复到 -h 指定的MongoDB服务器 的 -d指定的数据库里
$ sudo mongorestore -h 192.168.37.90 -d test --dir ./mongo_data/test




------- 爬虫的并发控制


一个CPU在同一个时间片，只能执行一个任务。

并行 ： 多个CPU同时执行多个任务（CPU >= 任务数）

任务1： --------------
任务2： --------------
任务3： --------------

C10K
Intel 超线程 ： 一个CPU核心，可以有两个任务执行单元
AMD

并发 ： 单个CPU需要执行多个任务 （CPU < 任务数）

任务1：-----         -----
任务2：     -----         -----
任务3：          -----


进程、线程 本质都是 操作系统执行任务的调度单位。

多进程 ： 并行
每个进程都有自己独立的内存空间，不同进程不能共享内存空间，所以多进程的任务开销太大。
multiprocessing


多线程 ： 并发
多个线程共享同一个进程的内存空间，数据通信、信号、切换开销极小。  抢占式获取系统资源
互斥锁：让多个线程安全有序的访问内存空间的机制。

threading、
multiprocessing.dummy

GIL 全局解释器锁：在一个解释器环境下，一次只能运行一个线程。
从根本上杜绝了多个线程访问内存空间的安全问题。

GIL 在IO阻塞的时候，会自动释放，尝试让其他线程工作。


多协程 ： 并发
协程 本质是 函数/方法，由程序员调度。

gevent
gevent.monkey.patch_all()
将Python底层的网络库(socket、select)打个补丁，让他们在处理网络IO的时候，按异步的方式执行。


同步、异步  : 执行方式
阻塞、非阻塞 ： 执行状态
)


["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]




node_list = "//div[@class='info']"

for node in node_List:
    title = node.xpath("./div[1]/a/span[1]/text()")[0]
    score = node.xpath(".//span[@class='rating_num']/text()")[0]







第七天：


import threading

thread_list = []
thread = threading.Thread(target, args)
thread.start()
thread_list.append(thread)


for thread in thread_list:
  thread.join()


from multiprocessing.dummy import Pool

from gevent.pool import Pool


pool = Pool(20)

1. 迭代list的每个元素，并将元素做为参数传递给func执行，最后将所有的返回值统一保存在 resutl_list
result_list = pool.map(func, list, list)

2. 迭代list的每个元素，并将元素做为参数传递给func执行，最后将所有的返回值的列表一起传递给callback处理
pool.map_async(func, list, callback)

3. 将args做为参数传递给func执行（apply是同步阻塞方式执行，不是异步）
result = pool.apply(func, args)

4. 将args做为参数传递给func执行，并将返回值传递给callback执行
pool.apply_async(func, args, callback)


# 协程池不需要close
pool.close()
pool.join()





1. 通过Python调用浏览器解析页面，处理动态数据加载（AJAX、JavaScript）

selenium 可以执行浏览器的平台，并且可以执行浏览器的各种动作事件
PhantomJS 就是一个无界面headless的浏览器
Chrome 有界面的浏览器

Selenium + PhantomJS
Selenium + Chrome

# 导入webdriver
from selenium import webdriver
# 创建浏览器对象
driver = webdriver.PhantomJS()  # 无界面的 PhantomJS
driver = webdriver.Chrome()  # 默认有界面的 chrome
# 发送浏览器的网页请求
driver.get("http://www.baidu.com/")
# 获取网页渲染后的源码
html = driver.page_source



1. 发送请求（如何模拟浏览器的请求，发送给网站服务器，获取响应 urllib2 requests）
2. 提取数据（从响应里提取数据re lxml bs4 jsonpath，可能会涉及js加密 js2py selenium+PhantomJS）
3. 保存数据（json、csv、mongodb，数据去重）
4. 提高并发量（多线程、协程）
5. 反爬处理（请求报头、代理IP、访问频率、验证码）




https://www.douyu.com/directory/all

node_list = xpath("//div[@id='live-list-content']//div[@class='mes']")

for node in node_list:
  room_name = node.xpath('.//h3[@class="ellipsis"]/text()')
  type_name = node.xpath('.//span[@class="tag ellipsis"]/text()')
  directory_name =node.xpath('.//span[@class="dy-name ellipsis fl"]/text()')
  people_number = node.xpath('.//span[@class="dy-num fr"]/text()')



if "shark-pager-next shark-pager-disable shark-pager-disable-next" in html:
  break
else:
  下一页： class="shark-pager-next"




2. 通过抓包工具抓取网页数据包，也可以抓取移动端H5、APP里数据


Fiddler、Charles  本地代理服务器 127.0.0.1：8888

数据加密：
  网页通过JavaScript，可以通过分析js代码进行破解；
  移动端app通过客户端软件代码（java、oc、swift），可以通过反汇编逆向工程进行处理

Fiddler 是Windows平台




Fiddler设置：
电脑浏览器抓包：
1. 点开Options菜单，点击HTTPS，允许电脑抓取HTTPS通信包，并安装Fiddler信任证书
2. 点开Options菜单，点击Connections，设置 允许远程计算机链接
3. 重新启动Fiddler
4. 打开浏览器，使用SwitchOmega 设置代理为 127.0.0.1:8888 即可访问HTTPs页面抓包

手机抓包：
1. 手机和电脑必须在同一个网段下（表示可以通过同一个路由器链接）
2. 手机设置 WiFi的代理为 电脑的IP代理，端口号 8888
3. 访问 http://电脑的ip:8888  下载手机的证书



Charles设置：
电脑浏览器抓包：
1. 安装后，替换安装目录下的 lib 下的 charles.jar 用于破解。
2. 点开Proxy菜单，选择Proxy settings... 打开HTTP抓包，默认8888端口
3. 点开Proxy菜单，选择SSL Proxing settings... 打开 https抓包，添加监听 *.*
4. 点开Help菜单，选择SSL Proxying，安装Charles信任证书
5. 打开浏览器，代理设置为 127.0.0.1:8888 即可访问HTTPs页面抓包


手机抓包：
1. 手机和电脑必须在同一个网段下（表示可以通过同一个路由器链接）
2. 手机设置 WiFi的代理为 电脑的IP代理，端口号 8888
3. 手机浏览器访问：http://www.charlesproxy.com/getssl 安装证书即可。


Wireshark:




移动端抓包：
1. 手机和电脑 必须在同一个网段下（WiFi）
2. 电脑共享热点，让手机连接
3. 在电脑上安装（Android、iOS模拟器）来实现数据抓包
          网易MuMu、夜神、雷电

移动端配置：
第一步，安装Fiddler证书，访问PC端ip:8888 下载安装证书
第二步，通过WLAN 修改手机端的 WiFi 代理为 pc端 ip:8888





3. 验证码处理，Tesseract OCR、打码平台

打码平台：

http://www.ruokuai.com/client/index?698490
http://www.yundama.com/
http://jiyan.c2567.com/docs/default.html
https://www.aliyun.com/ss/?k=%E9%AA%8C%E8%AF%81%E7%A0%81


自然语言处理
图像识别
语音识别








第八天：




框架一定是方便使用。


函数 - 类 - 模块 - 包 - 框架


1. 发送请求，获取响应  send_request(request)
    urllib2、requests
2. 解析响应，提取数据  parse_page(response)
    re、xpath、bs4、jsonpath
3. 保存数据  save_data(item)
    mysql、redis、mongodb、json、csv、xml


Scrapy 提供了三大对象：

1. Request对象
2. Response对象
3. Item对象


Scrapy 提供了五个核心组件：

1. Spider爬虫：  -1. 提供第一批url地址，  -2. 提供的解析响应的方法（url、item）
2. Scheduler ： -1. 对每个请求做去重处理， -2. 将去重的请求放入请求队列（之后会交给下载器）
3. Downloader ： （并发）发送请求，返回响应
4. Pipeline： 接收并保存item数据
5. Engine ： 负责调用各个组件和传递数据，保证框架的正常工作。


Scrapy 提供了两个可选的中间件：

1. 下载中间件 Downloader Middlewares ：  引擎 <->  下载器  (请求、响应 的预处理)
2. 爬虫中间件 Spider Middlewares ： 爬虫 <-> 引擎 （请求、item数据、响应）

组件A  - 中间件  -  组件B


Scrapy对应下载失败的请求，会有重试操作，总共重试 3 次。






Scrapy的 response 响应主要属性：

response.url  # 响应 url地址
response.haeders # 响应报头
response.body # 网页原始编码字符串
response.text # 网页Unicode编码字符串
response.status # 响应的状态码

response.xpath("//title/text()") 返回所有匹配结果的表达式列表

再通过 extract() 或 extract_first() 获取字符串内容

extract() : 返回所有结果的字符串列表（没有匹配到数据，返回空列表）
extract_first() ： 返回第一个结果的字符串列表（如果没有匹配到数据，返回None）


from lxml import etree

class Response(object):
    def __init__(self):
        self.url = "xxx"
        self.headers = {}
        self.body = requests.get().content
        self.text = requests.get().text


    def xpath(self, rule_str):
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule_str)


response = Response()
result_list = response.xpath("//title/text()")





Scrapy 常用的命令和使用流程：

1. 新建项目
scrapy startproject Baidu

2. 定义items.py的数据字段

3. 新建爬虫
scrapy genspider baidu baidu.com

4. 编写spiders/里的爬虫代码：

5. 编写pipelines的管道代码；

6. 通过settings.py 启用相关配置信息

7. 执行爬虫
scrapy runspider baidu.py
或 scrapy crawl baidu


注意：
1. 如果有多个爬虫执行，所有的爬虫共享 items.py、pipelines.py、middlewares.py、settings.py 文件；

2. Scrapy支持基本的文件格式保存方案：json、csv、xml、jl等，执行时 scrapy crawl xxxx -o xxxx.json 输出

3、 除非是自定义函数 调用或返回数据，否则在Scrapy的任何组件里 return/yield，都是将数据返回给引擎处理，引擎会自行判断数据类型，并传递给对应的其他组件。





http://www.itcast.cn/channel/teacher.shtml

"//div[@class='li_txt']"
h3
h4
p



https://hr.tencent.com/position.php?&start=0 += 10   <= 2810

node_list = //tr[@class='even'] | //tr[@class='odd']

for node in node_list:
    position_name = node.xpath("./td[1]/a/text()").extract_first()
    position_link = node.xpath("./td[1]/a/@href").extract_first()
    position_type = node.xpath("./td[2]/text()").extract_first()
    people_number = node.xpath("./td[3]/text()").extract_first()
    work_location = node.xpath("./td[4]/text()").extract_first()
    publish_times = node.xpath("./td[5]/text()").extract_first()



第九天：


Scrapy处理翻页数据抓取三种方案：
  根据业务场景灵活选择。

1. 分析网页url地址变化规律，在通过自增量拼接完整的url，发送请求获取响应，可以根据响应内容 或 响应状态码 做为停止条件。
  - 适合动态页面 json 文件的抓取，不依赖网页 <a> 标签


2. 分析网页下一页链接，并提取链接发送请求获取响应，再判断是否是最后一页做为停止条件。
  - 适合 html 文件的抓取，依赖网页 <a> 标签
  - 对于页码经常变动的网页，可以灵活获取所有页面


3. 将所有需要发送的请求url地址，全部存在 start_urls 中，做为第一批请求全部交给下载器发送，下载器根据并发量进行处理，可以充分利用Scrapy的高并发。
  - 可以通过 读取文件、数据库，或 列表推导式的方式，获取所有的url地址




Scrapy处理多级页面的数据抓取：

1. 列表页 和 详情页 的数据保存在 不同的 item 中
  - 在 items.py 里构建不同的 item 类
  - 在 spider 中处理数据提取，并保存在不同的item对象中，并 yield item 给管道
  - 在 pipelines 里处理数据分类（可以根据item字段，或 isinstance() 判断），分别处理数据


2. 列表页 和 详情页 的数据保存在 同一个 item 中
  - 在 items.py 里构建一个可以存储所有字段数据的 item 类
  - 在spider中处理数据提取，保存一级页面数据，并通过构建 Request() 的meta参数，传递当前的item
  - meta 接收一个字段，可以包含多个键值对，并且做为 该请求 对应的响应 的meta属性，传递到回调函数里
  - 根据需求，可以继续向下传递，直到所有的数据提取完毕，再 yield item



def start_requests(self):
  for url in self.start_urls:
    yield scrapy.Request(url, callback=self.parse, dont_filter=True)

1. start_requests() 方法用以处理 start_urls里的每个请求发送方式，可以重写该方法自定义处理。
2. 默认start_urls里的请求 不去重，dont_filter默认为False（去重）dont_filter(不去重)





CrawlSpider：

start_urls 里的响应，默认 follow 是 True

rules = [
    Rule(  LinkExtractor(allow=r'start=\d+'),  follow=True),
    Rule(  LinkExtractor(allow=r'position_detail\.php\?id=\d+'),  callback='parse_detail',  follow=False),
]


rules 是一个可以存储多个Rule规则的 列表/元组，引擎会迭代 rules 处理每个Rule

每个 Rule 规则，都表示一种 网页链接提取方式 和 响应处理方式

    1. LinkExtractor() 表示链接提取方式，并且发送这些链接的请求，返回的响应根据 callback 和 follow 决定：

    2. callback 表示 这些响应交给指定的 回调函数 解析

    3. follow 是一个 bool 值 :

       - follow = False 表示这些响应，不再通过 任何Rule 的 LinkExtractor 提取链接

       - follow = True 表示这些响应，会经过 每个Rule的 LinkExtractor 提取链接，再次发送这些新链接请求，这些新链接的响应 会根据所属的follow值判断，如果为 True 会继续经过 每个Rule的 LinkExtractor 提取链接，一直递归下去..

          当所有的能被提取的链接全部发送过，且没有新的请求了，程序结束。



Spider

CrawlSpider 专为整站抓取而设计的爬虫类：

start_urls

首页  （提供一级链接）  Rule(LinkExtractor(allow=r'一级页面的规则'), follow=True)
一级页面（提供二级链接）Rule(LinkExtractor(allow=r'二级页面的规则'), follow=True)
二级页面（提供三级链接）Rule(LinkExtractor(allow=r'三级级页面规则'), follow=True)
三级页面（提供四级链接）Rule(LinkExtractor(allow=r'四级页面的规则'), callback="parse_page", follow=False)
四级页面（提供数据）

没有callback，默认follow=True
有callback，默认follow=False



用户画像
精准营销

今日头条  推荐系统



IP代理：
1. 抓取网上免费代理，测试
2. 代理供应商提供的代理（收费）
3. ADSL拨号，每次重新拨号会更换本地IP，但是会有1~3秒延迟
4. VPN/VPS 虚拟主机（翻墙爬取国外网站）
5. Tor网络（暗网） 洋葱浏览器


pip install fake_useragent

from fake_useragent import UserAgent

ua_obj = UserAgent()
ua_obj.ie
ua_obj.chrome
ua_obj.random


http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset=0  += 100


room_id
vertical_src
nickname
anchor_city
image_path


1. 如果有重复图片、文件，保存到本地只有一份，后续改名只能成功一次，后面再改名。


2. 用商品名称做为图片名保存，如果图片名里有"/"，则保存时会当作路径结点使用。
  file_name = "Huawei Mate20 Pro 8GB/128GB 月光灰"
  if "/" in file_name:
     file_name.replace("/", "-")





模拟登陆：
1. 直接发送账户密码的POST请求，记录cookie，再发送其他页面的请求
2. 先发送登录页面的get请求，获取登录参数，再发送登录的post请求，提交账户密码和登录参数，并记录cookie，再发送其他页面的请求
3. 直接将cookies保存在请求报头里，直接发送附带登录状态的请求，获取页面。





Scrapyd远程部署和执行爬虫、停止爬虫、监控爬虫运行状态


1. 安装客户端和服务器端的工具：
客户端：pip install scrapyd-client
服务器端： pip install scrapyd     # 6800

2. 服务器端开启scrapyd服务（提供一个监听6800端口的web）
  修改 default_scrapyd.conf 配置文件里的 bind_address 为 0.0.0.0
  再开启服务
  ubuntu: $ scrapyd


以下全部是客户端的操作：

3. 修改scrapy项目的scrapy.cfg文件，添加 配置名称和url
  [deploy:scrapyd_Tencent3]
  url = http://192.168.37.80:6800

4. 将项目部署到指定scrapyd服务器上（每次本地有任何变动，必须重新部署一次）
scrapyd-deploy scrapyd_Tencent3 -p Tencent3


5. 启动指定 scrapyd服务上的 指定项目的 指定爬虫（会生成该爬虫的jobid值，用于区分）
curl http://192.168.37.80:6800/schedule.json -d project=Tencent3 -d spider=tencent_crawl


6. 停止指定 scrapyd服务上的 指定项目的 指定爬虫
curl http://192.168.37.80:6800/cancel.json -d project=Tencent3 -d job=jobid值

scrapyd-web





第十一天：scrapy_redis分布式组件



scrapy shell 两种用法：

# 通过-s参数 ，单独添加 settings里指定的字段
1. scrapy shell "http://www.baidu.com/" -s USER_AGENT="xxx"

# 进入scrapy shell, 手动构建请求（添加headers和cookies）并发送，可以处理需要特殊参数的页面。
2. scrapy shell
> request = scrapy.Request(url, headers, cookies)
> fetch(request)
> response.body




scrapy原本不支持分布式，因为请求不能共享

分布式爬虫： 在不同的 硬件环境 和 网络环境 下，实现请求队列共享。


from hashlib import sha1
s1 = sha1()
s1.update("url")
s1.update("method")
s1.update("params")
s1.update("formdata")

fp = s1.hexdigest()



requests + xpath + 多线程/协程 + 分布式（断点续爬）

scrapy:

    # 指纹处理
    fp_set = set()


    if fp in fp_set:
        return

    fp_set.add(fp)


    # 请求处理
    from collections import deque
    双向队列，可以实现先进先出 FIFO， 后进先出  LIFO


scrapy_redis:


    #### 指纹处理
    import redis

    client = redis.Redis(host, port)

    # 向set中添加数据
    client.sadd("fp_set", fp)

    # 判断redis的set里是否有指定数据，有则返回True，没有返回False
    client.sismember("fp_set", new_fp)



    #### 请求处理
    import pickle

    # 将请求队列序列化为字符串，方便存储到数据库里
    request_str = pickle.dumps(request)
    # 在使用请求时，通过loads()将字符串反序列化为请求队列，就可以发送
    request = pickle.loads(request_str)

    # 从左往右放+从右往左取，表示先进先出
    # lpush+rpop； FIFO
    # rpush+lpop： FIFO
    client.lpush("request_queue", request_str)
    request_str = client.rpop("request_queue")




scrapy-redis 分布式组件： 用来替换scrapy原本在内存里存储数据的部分，转存到redis数据库里保存，以便所有爬虫端读取。

scrapy-redis在redis数据库里提供：

请求指纹集合  ： 在同一个redis数据库里对请求判重，将不重复的请求添加到请求队列中；
请求队列     ： 在同一个redis数据库里保存请求，方便其他爬虫端读取请求，实现分布式抓取
item队列    ： 在同一个redis数据库里，保存所有的抓取结果


scrapy-redis 将所有请求pop出并发送，请求队列为空，但程序不会退出，而是等待是否有其他爬虫端会提供新的请求，或等待用户指定新的请求任务（可以通过ctrl+c退出）

分布式，断点续爬



RedisSpider、RedisCrawlSpider


少了 start_urls，
多了 redis_key = "start_urls_key"

lpush start_urls_key http://www.baidu.com/ http://www.qq.com/



在线安装：pip install scrapy_redis   # pypi.org
离线包安装：pip install scrapy_redis_linux_amd64_1_2.whl
源码安装：python setup.py install


不是非要写分布式爬虫，才会用到scrapy_redis，只要需求需要 保存请求指纹、请求队列、item数据到redis数据库里，就可以使用scrapy_redis，支持断点续爬



RedisSpider和RedisCrawlSpider:

    1. 导入并继承RedisSpider和RedisCrawlSpider，删除start_urls，添加redis_key;

    2. redis_key 对应 redis数据库的一个 键名，当程序启动后，某个爬虫端会读取到这个键对应的 url 列表，并保存到该爬虫的start_urls中;

    3. 该爬虫端会发送start_urls请求，返回并解析响应，提取更多的url请求，再保存到redis数据库中;

    4. redis数据库会分配新的请求，给所有爬虫端执行，实现分布式抓取;

    5. 每个爬虫端在执行时，会从redis里获取判重后的请求，也会提取新的请求和item 保存到redis数据库里;

    6. 当所有请求发送完毕后（即请求队列为空），程序不会关闭，而是继续等待其他爬虫端提交的新请求，或用户指定新的请求任务。

    通过redis_key 提供第一批url地址请求 或 指定新的请求任务：
    > lpush myspider:start_urls http://www.baidu.com/ http://www.qq.com/



#settings.py 的设置

# 1(必须). 使用了scrapy_redis的去重组件，在redis数据库里做去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 2(必须). 使用了scrapy_redis的调度器，在redis里分配请求
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 3(必须). 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True

# 4(必须). 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item
# 这个已经由 scrapy-redis 实现，不需要我们写代码，直接使用即可
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 100
}

# 5(必须). 指定redis数据库的连接参数
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# 6.如果不启用则按scrapy默认的策略
#  -1. 默认的 按优先级排序(Scrapy默认)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#  -2. 可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
#  -3. 可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'




编写 scrapy-redis分布式爬虫代码：

1. 先将代码写成 scrapy版本
2. 修改 settings.py，添加scrapy_redis的组件
3. 修改 spider 文件：
    -1 导入并继承 RedisSpider、RedisCrawlSpider
    -2 删除 start_urls，避免多个爬虫端发送重复请求
    -3 添加 redis_key ，表示数据库接收第一批url的键
4. 启动爬虫，在数据库通过 lpush 添加第一批请求url地址即可。





AQI

# 首页
base_url = "https://www.aqistudy.cn/historydata/"
start_urls = [base_url]


# 提取所有城市的链接 （静态页面）
"//div[@class='all']//a/@href"

# 提取某个城市的所有 月份链接 （动态页面）
"//tbody/tr/td[1]/a/@href"

# 提取某个月的 所有天数据（动态页面）
tr_list = xpath("//tbody/tr")
tr_list.pop(0)

for tr in tr_list:
    日期 = tr.xpath("./td[1]/text()")
    AQI = tr.xpath("./td[2]/text()")
    质量等级 = tr.xpath("./td[3]/span/text()")
    PM2.5 = tr.xpath("./td[4]/text()")
    PM10 = tr.xpath("./td[5]/text()")
    SO2 = tr.xpath("./td[6]/text()")
    CO = tr.xpath("./td[7]/text()")
    NO2 = tr.xpath("./td[8]/text()")
    O3_8h = tr.xpath("./td[9]/text()")

    yield item


scrapy + scrapy_redis + Selenium + Chrome : 终极大招，可以处理任何页面的渲染，同时效率很高。


Spider和CrawlSpider
RedisSpider和RedisCrawlSpider



requests + xpath + 多线程/协程 + 分布式（redis）

请求指纹： url、method、params、formdata   sha1() 指纹
指纹集合： set    - sadd()    sismember()

请求对象： pickle   dumps()  loads()
请求队列： list    lpush+rpop   rpush+lpop     FIFO  LIFO
          zset    zadd




scrapy + scrapy_redis


pip install retrying








