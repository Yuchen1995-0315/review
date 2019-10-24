"""
regex.py  re模块函数示例1
"""
import re
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)"

# re模块调用
l = re.findall(pattern,s)
print(l)

# compile对象调用
regex = re.compile(pattern,flags=0)
l = regex.findall(s,0,15)
print(l)

# 按照正则表达式匹配内容切割字符串
l = re.split(r"[:,]",s,2)
print(l)

# 使用指定字符串替换匹配内容
# s = re.sub(r":",'--',s,1)
s = re.subn(r":",'--',s,1)
print(s)



