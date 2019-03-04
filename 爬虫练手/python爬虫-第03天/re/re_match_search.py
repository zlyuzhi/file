import re
s = "abcd1234bcda4321"
pattern = re.compile(r"\d+")
m = pattern.match(s) # 从文本开头进行匹配，只匹配一次
print(m)

m = pattern.match(s, 4)
print(m.group())

m = pattern.search(s) # 从文本任意位置开始匹配，只匹配一次
print(m.group())

%hist -f re_match_search.py
