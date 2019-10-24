"""
udp客户端，使用struct打包数据发送
id   姓名    年龄   身高
int  str    int   float
"""

from socket import *
import struct

ADDR = ('127.0.0.1',8888) # 服务端地址

# 数据格式定义
st = struct.Struct("i16sif")

# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)

while True:
    print("========================")
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("AGE:"))
    score = float(input("SCORE:"))
    # 打包发送数据
    data = st.pack(id,name,age,score)
    s.sendto(data,ADDR)




