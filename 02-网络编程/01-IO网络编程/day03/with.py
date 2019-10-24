"""
with.py
使用with 语句打开文件
"""

with open('3.txt') as f:  # 等于 f = open('3.txt')
    data = f.readline()
    print(data)

# with语句块结束 f 自动销毁 不需要close