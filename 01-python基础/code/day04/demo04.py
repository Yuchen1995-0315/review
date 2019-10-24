"""
    字符串
    练习:exercise05
"""
# 1. 不可变
# 原因：如果在原有内存上修改数据，可能破坏其他对象的内存。
name = "孙悟空"
name = "悟空"
print(name)# "齐天大圣"

# 2. 编码:让字符 转换为 数字
# 字 --> 数
number = ord("a")
print(number)#97
# 数 --> 字
char = chr(97)
print(char)# a

