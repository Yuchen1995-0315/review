"""
http_test.py
http请求响应演示
"""

from socket import *

# 创建tcp套接字
s = socket()
s.bind(('127.0.0.1',8000))
s.listen(3)

print("Listen the port 8000...")
c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)  # http请求
print(data.decode())

# 组织http响应
response = """HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8

哈哈哈啊
"""
c.send(response.encode())