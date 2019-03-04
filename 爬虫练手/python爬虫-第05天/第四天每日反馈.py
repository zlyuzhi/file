姓名  意见或建议
*** 老师，这几天都是爬取文本，能不能教教视频音频的爬取技巧，例如爱奇艺等视频网站，怎么着手分析，工作中，那种类型的数据需求居多

文本数据（HTML、json、xml、JavaScript、txt） js2py.eval_js()
图片（jpg、png、gif...)：公共的图片查看器，按 wb 保存即可。
音频（mp3、wav、aac、flac、ape）：公共的音频解码器，按 wb 保存即可。
视频（mp4、wmv、avi、rmvb）：公共的视频解码器，按 wb 保存即可。

<embed src="https://imgcache.qq.com/tencentvideo_v1/playerv3/TPout.swf?max_age=86400&v=20161117&vid=a0794yqe8dn&auto=0" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>


<iframe frameborder="0" src="https://v.qq.com/txp/iframe/player.html?vid=a0794yqe8dn" allowFullScreen="true"></iframe>


*** 动态页面通过抓包抓取数据，是不是不需要用xpath和正则表达式语法进行页面代码匹配了？
*** 现在爬虫工作好找吗
    数据采集+数据计算+数据分析+数据可视化   +数据挖掘+机器学习   +深度学习

*** 今后工作了做爬虫也是团队开发吗

User-Agent、代理IP、Cookie
*** 老师能讲一下如果以后要爬的网站要携带cookie，或者需要用户名或者密码等信息的网站该怎样去爬

*** 转来转去,类型之间,编码之间,感觉好乱啊,老师能帮忙捋一捋吗,谢谢!

*** 对于编码、lxml、xpath、etree，Jasonpath、beautifulsoup等等还是很乱

#coding:utf-8

python代码里的文字，都是utf-8

unicode_str = gbk_str.decode("gbk")
utf8_str = unicode_str.encode("utf-8")


lxml、xpath、etree

from lxml import etree
html_obj = etree.HTML(html)
html_obj.xpath()


from jsonpath import jsonpath
name_list = jsonpath(python_obj, "$..name")


from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")

node_list = soup.find_all()
node_list = soup.select()


*** 老师可不可以把 Unicode, python2, python3 的字符, json字符的相关问题能不能用图解来描述一下,感觉已经云里雾里了

    json 模块：
    xpath()、beautifulsoup() 里面的字符串数据都是 Unicode    '\u2f4a\u8a9c'
    json_str = json.dumps([unicode_str, unicode_str], ensure_ascii=False)
    ascii 文字， import sys
                reload(sys)
                sys.setdefaultencoding("utf-8")

*** 老师很好
*** 1、正则表达式中 特殊构造有点不理解
    2、这个编码上了几天就晕了几天，并没有像你之前说的 会越来越清晰。可能和你理解的有偏差，还是做个总结吧。  求其是python2和3的区别。

*** 老师,有办法可以破解VIP账号吗, 爬虫 和 黑客技术有什么不同?

