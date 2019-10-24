"""
空洞文件
"""
f = open('test','wb')

f.write(b's')
f.seek(1024*1024,2)  # 从尾部向后移动1M
f.write(b'e')

f.close()
