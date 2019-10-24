"""
 使用udp和struct模块完成

      1. 从客户端循环录入学生信息，包含

          id   姓名    年龄   身高
          int  str    int   float

      2. 将信息打包发送给服务端

      3. 在服务端将学生信息写入到一个文件中，每个学生信息一行
"""
from socket import *
import struct

# 与客户端商定一致的格式
st = struct.Struct("i16sif")

# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 打开文件
f = open('student.txt','a')

while True:
    data,addr = s.recvfrom(1024)
    data = st.unpack(data) # 数据解包

    # data写入文件
    info = "%d    %-10s   %d   %.1f\n"%data
    f.write(info)
    f.flush()







