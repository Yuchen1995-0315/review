"""
二级子进程
"""
import os,time

def fun1():
    time.sleep(2)
    print("事件1")

def fun2():
    time.sleep(3)
    print("事件2")

pid = os.fork()
if pid == 0:
    p = os.fork() # 创建二级子进程
    if p == 0:
        fun2()  # 二级子进程做一件
    else:
        os._exit(0) # 退出一级子进程
else:
    os.wait() # 等一级子进程退出
    fun1() # 父进程做一件
