"""
模拟僵尸进程产生
"""

import os,sys

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit()
else:
    while True:
        pass