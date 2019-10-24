"""
使用udp完成： 从客户端可以循环的输入单词，
      得到单词解释打印（如果单词不存在则提示不存在）

服务端功能: 提供数据处理逻辑处理
"""

from socket import *

# 查单词函数
def find_word(word):
    # 以读方式打开
    f = open('dict.txt')
    # 每次获取一行
    for line in f:
        wd = line.split(' ', 1)[0]
        # 如果遍历到的单词已经大于目标单词，就不必查找了
        if wd > word:
            f.close()
            return "没有找到该单词"
        # 比较是不是输入的单词
        elif word == wd:
            f.close()
            return line
    else:
        f.close()
        return "没有该单词"


# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

# 循环收取单词
while True:
    data,addr = s.recvfrom(128) # 收单词
    # 调用函数得到查询结果
    result = find_word(data.decode())
    s.sendto(result.encode(),addr)

s.close()