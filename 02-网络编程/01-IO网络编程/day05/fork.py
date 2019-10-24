"""
fork.py fork创建进程演示1
"""

import os
from time import sleep

# 通过函数发起进程创建申请
pid = os.fork()

if pid < 0:
    print("Create prcess failed")
elif pid == 0:
    # 子进程执行部分
    sleep(3)
    print("The new process")
else:
    # 父进程执行部分
    sleep(4)
    print("The old process")
print("Fork test over")
