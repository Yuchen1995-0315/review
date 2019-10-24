"""
seek.py 文件偏移量演示

总结： r w  open打开文件偏移量在开头
      a 打开文件偏移量在结尾
      通常以二进制方式打开操作文件偏移量
"""
f = open('test','wb+')
f.write(b"Hello world")
f.flush()
print("文件偏移量：",f.tell())

# 操作文件偏移量位置
f.seek(-3,1)

data = f.read()
print(data)
f.close()