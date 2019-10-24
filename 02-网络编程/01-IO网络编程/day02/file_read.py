"""
file_read.py
读操作演示
"""

# 打开文件
f = open('file.txt', 'r')  # 默认 ‘r’

# read 读取
# data = f.read(5)
# print(data)

# 循环读取
# while True:
#     # 文件到结尾会读出空字串
#     data = f.read(1)
#     if not data:
#         break
#     print(data,end='')

# readline 读取一行
# data = f.readline(5) # 读取 5 个字符
# print(data)
# data = f.readline()
# print(data)

# readlines 读取多行内容形成列表
# data = f.readlines(8)  # 读到第8个字符所在的行
# print(data)

# 迭代方式每次读取一行
for line in f:
    print(line) # 每次迭代内容为一行


f.close()
