"""
编写一个服务端和一个客户端，
       从客户端将一个文件发送给服务端，
       文件类型可以为文本也可以是而二进制文件
"""

from socket import *

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

"""
思路 ： 先recv()接收内容，write()写入到一个文件中
"""

# 打开文件
filename = c.recv(1024).decode() # 接收文件名字
f = open("/home/tarena/"+filename,'wb')

# 循环接收内容，写入文件
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()









