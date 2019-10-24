"""
编写一个程序，向一个文件中不断写入如下内容：

   1.  2019-1-1  18:18:18
   2.  2019-1-1  18:18:20
   3.  2019-1-1  18:18:30

要求每隔2s 写入一条，每条占一行， 行号 + 当前时间
如果程序结束，再次启动时要求行号能够衔接
"""

import time

f = open('log.txt','a+')

n = 0  # 行号
# 获取行数
f.seek(0)
for line in f:
    n += 1

while True:
    n += 1
    time.sleep(2)
    s = "%d. %s\n"%(n,time.ctime())
    f.write(s)
    f.flush() # 随时查看








