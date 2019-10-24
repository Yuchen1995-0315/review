from socket import *

s = socket()
s.connect(('127.0.0.1',8888))

"""
读取文件内容，发送给服务端
"""

filename = input("File:")

s.send(filename.encode()) # 发送文件名

f = open(filename,'rb')
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()