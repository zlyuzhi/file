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
