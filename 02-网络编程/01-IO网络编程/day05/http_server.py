"""
httpserver1.0
1. 获取来自浏览器的http请求
2. 判断请求内容如果是 / 则将index.html给客户端
3. 如果不是/ 则一律返回404响应
思路 ： tcp循环模型不断接收请求
       提取http请求中的请求内容，做判断
"""
from socket import *

# 客户端处理函数
def request(connfd):
    # 获取http请求
    data = connfd.recv(4096)
    # 浏览器断开
    if not data:
        return
    # 请求行
    request_line = data.decode().split('\r\n')[0]
    # 请求内容
    info = request_line.split(' ')[1]

    # '/' 返回 index.html
    if info == '/':
        with open('index.html','r') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += 'Content-Type: text/html\r\n'
            response += '\r\n'
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += 'Content-Type: text/html\r\n'
        response += '\r\n'
        response += "<h1>Sorry...</h1>"
    # 发送给浏览器
    connfd.send(response.encode())

# 搭建tcp模型
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(3)

# 循环接收请求
while True:
    connfd, addr = sockfd.accept()
    print("Connect from",addr)
    request(connfd) #  处理客户端请求

sockfd.close()












