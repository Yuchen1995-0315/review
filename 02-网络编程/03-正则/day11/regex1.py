"""
regex.py  re模块函数示例2
"""
import  re

s = "2019年10月1日举行国庆阅兵，庆祝建国70周年，祖国万岁。"
pattern = r"\d+"

# 返回匹配结果的迭代对象
# r = re.finditer(pattern,s)
# for i in r:
#     print(i.group()) # 迭代到的内容为匹配结果的match对象


# 完全匹配一个字符串
m = re.fullmatch(r'.+',s)
print(m.group())

# 匹配开始位置
m = re.match(r'\w+',s)
print(m.group())

# 匹配第一处
m = re.search(r'\d+',s)
print(m.group())
