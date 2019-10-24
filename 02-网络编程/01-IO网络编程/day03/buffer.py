"""
buffer.py 文件读写缓冲机制演示
"""

f = open('test','w',1)  # 行缓冲，换行刷新缓冲

while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
    f.flush()  # 人为刷新

f.close()  # 文件结束会刷新缓冲