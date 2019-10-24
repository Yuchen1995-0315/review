"""
file_write.py
文件写操作
"""

# f = open('file.txt','w') # 写方式打开
f = open('file.txt','a') # 追加写

# write写操作
# f.write("AID1908\n".encode())
# f.write("哎呀，干啥".encode())

# 将列表每一项写入文件
l = ['hello kitty\n','哈哈哈']
f.writelines(l)

f.close()