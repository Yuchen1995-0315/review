"""
使用多个线程从不同的地方拷贝一个文件
每个线程负责拷贝文件的一部分
"""
from threading import Thread,Lock
import os
from time import sleep

urls = ["/home/tarena/桌面/",
        "/home/tarena/文档/",
        "/home/tarena/图片/",
        "/home/tarena/下载/",
        "/home/tarena/视频/",
        "/home/tarena/音乐/"
]

lock = Lock() # 锁

# 输入要下载的文件，判断urls列表中哪些地方有这个文件
# os.path.exists()
filename = input("要下载的文件:")
exp = []  # 存放有该文件的路径
for i in urls:
    if os.path.exists(i+filename):
        exp.append(i+filename)
path_num = len(exp) # 表示一共有几处可以拷贝

if path_num == 0:
    print("没有资源")
    os._exit(0)

# 获取文件大小，确定每个线程下载多少
file_size = os.path.getsize(exp[0])
block_size = file_size // path_num + 1

# 创建若干线程，每个线程拷贝一部分，拷贝过程封装为线程函数
fw = open(filename, 'wb')

def load(path,num):
    # path: 从哪个路径拷贝
    # num：拷贝的是第几块
    f = open(path,'rb')
    f.seek(block_size*(num - 1),0)
    data = f.read(block_size)

    with lock:
        fw.seek(block_size*(num - 1),0)
        sleep(0.1)
        fw.write(data)

    f.close()

num = 1
jobs = []
for path in exp:
    t = Thread(target=load,args=(path,num))
    jobs.append(t)
    t.start()
    num += 1

for i in jobs:
    i.join()



