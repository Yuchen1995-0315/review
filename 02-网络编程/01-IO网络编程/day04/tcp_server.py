"""
tcp_server.py  tcp套接字服务端流程
重点代码

注意 ： 注重功能流程和函数使用
"""

import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 端口立即重用 （bind之前设置）
sockfd.setsockopt(socket.SOL_SOCKET,
                  socket.SO_REUSEADDR,
                  1)

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 设置监听
sockfd.listen(5)

# 等待处理客户端连接
while True:
    print("等待连接...")
    try:
        connfd, addr = sockfd.accept()
        print("连接到", addr)
    except KeyboardInterrupt: # ctrl-c终止程序
        break
    # 收发消息
    while True:
        data = connfd.recv(1024)
        # if data == b'##':
        #     break
        if not data:  # data为空表示客户端断开
            break
        print("收到:", data.decode())
        n = connfd.send(b'Thanks')
        print("发送 %d 字节" % n)
    connfd.close()

# 关闭套接字
sockfd.close()
