import re
s = "abcd bcd. aaaa, mmm; .bcda"

# 指定多个分隔符，全文分隔
pattern = re.compile("[\s\.\,\;]")
pattern.split(s)
# 指定多个分隔符，可以连续分隔
pattern = re.compile("[\s\.\,\;]+")
pattern.split(s)
%hist -f re_split.py
