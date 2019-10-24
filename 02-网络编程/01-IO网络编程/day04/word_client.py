from  socket import *

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
sockfd = socket(type=SOCK_DGRAM)

# 循环收发消息
while True:
    word = input(">>")
    if not word:
        break  # 输入空客户端退出
    sockfd.sendto(word.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print(msg.decode())

# 关闭套接字
sockfd.close()








