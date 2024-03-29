"""
获取进程PID号
"""

import os

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid()) # 子PID
    print("Get parent PID:",os.getppid()) # 父PID
else:
    print("Get child PID:",pid) # 子PID
    print("Parent PID:",os.getpid()) # 父PID