"""
multiprocessing创建进程
1. 编写进程函数
2. 产生进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep

a = 1

# 进程函数
def fun():
    print("开始一个进程")
    sleep(2)
    global a
    print("a = ",a)
    a = 10000
    print("结束一个进程")

# 创建进程对象
p = mp.Process(target=fun)
# 启动进程,执行fun函数
p.start()

# 父进程事件
sleep(1)
print("父进程干点事")

# 回收进程
p.join()
print("a:",a)


"""
p = os.fork()
if p == 0:
    fun()
    os._exit()
else:
    os.wait()
"""







