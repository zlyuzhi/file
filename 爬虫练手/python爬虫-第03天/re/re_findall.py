import re

s = "abcd1234bcda4321"
pattern = re.compile(r"\d+")
pattern.findall(s)

text = "hahaha <div id='123'>Hello 123 World</div> -mmmm- <div id='123'>Hello 456 World</div> hahaha"

# 贪婪模式进行匹配（从第一个匹配到最后一个）,返回规则文本和匹配内容
pattern = re.compile("<div id='123'>.*</div>")
pattern.findall(text)

# 贪婪模式进行匹配（从第一个匹配到最后一个），只返回匹配内容
pattern = re.compile("<div id='123'>(.*)</div>")
pattern.findall(text)

# 非贪婪模式进行匹配，分别返回多个匹配内容
pattern = re.compile("<div id='123'>(.*?)</div>")
pattern.findall(text)

%hist -f re_findall.py
