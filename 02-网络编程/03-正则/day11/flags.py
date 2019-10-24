"""
flags.py 扩展标志位演示
"""
import re

s = """Hello 
北京
"""
# 只能匹配ascii字符
# regex = re.compile(r'\w+',flags=re.A)

# 大小写不区分
# regex = re.compile(r"[a-z]+",flags=re.I)

# . 匹配换行
# regex = re.compile(r'.+',flags=re.S)

# regex = re.compile(r"^北京",flags=re.M)

pattern = r"""\w+ # 匹配hello
\s+ # 匹配空格
\w+ # 匹配北京
"""
# 在正则内部 # 添加注释 同时使用多个flag则用按位或连接
regex = re.compile(pattern,flags=re.X | re.I)
l = regex.findall(s)
print(l)
