"""
套接字属性介绍
"""

from socket import *

# 创建套接字
s = socket()

# 设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('172.40.91.159',8888))
s.listen(5)
c,addr = s.accept()

print("地址类型:",s.family)
print("套接字类型:",s.type)
print("绑定地址:",s.getsockname())
print("文件描述符:",s.fileno())
# 获取客户端地址，同accept返回的addr
print("客户端地址：",c.getpeername())

c.recv(1024)
