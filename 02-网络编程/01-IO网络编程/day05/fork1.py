"""
fork.py fork进程演示2
"""

import os
from time import sleep

print("==============================")
a = 1

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process")
    print("a =",a)  # 父进程中a开辟了空间会被子进程获取
    a = 10000 # 只是修改自己空间中的a
else:
    sleep(1)
    print("Parent process")
    print("a:",a)

print("All a = ",a)
