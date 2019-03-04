import re

s = "hello 123, hello 456, byebye789"
pattern = re.compile("\w+\s\w+")
pattern.sub("bye bye", s)

# 分组匹配并取分组
pattern = re.compile("(\w+)\s(\w+)")
pattern.sub(" \1 \2 ", s)
pattern.sub("byebye \2 ", s)

# Unicode文本
s = u"hello世界，123, hello中国"

# 匹配中文部分
pattern = re.compile(u"[\u4e00-\u9fa5]+")
print(pattern.sub("", s))

# 匹配非中文部分
pattern = re.compile(u"[^\u4e00-\u9fa5]+")
print(pattern.sub("", s))

%hist -f re_sub.py
