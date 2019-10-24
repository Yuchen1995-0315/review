"""
wait.py 处理僵尸进程
"""

import os,sys
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sleep(2)
    sys.exit(1)
else:
    # 阻塞等待子进程结束，处理子进程退出
    p,status = os.wait()
    print("p:",p)
    print('status:',status) # 子进程退出状态×256
    while True:
        pass