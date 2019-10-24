"""
编写一个程序，input输入一个文件名称(可以包含路径)
        将该文件拷贝到主目录下，
        注意文件是文本文件还是二进制文件不确定
        （不允许一次将文件内容全部读写）
"""
# 输入文件名称
filename = input("File:")

try:
    fr = open(filename,'rb') # 二进制打开
except FileNotFoundError as e:
    print(e)
else:
    file = filename.split('/')[-1]
    fw = open("/home/tarena/"+file,'wb')
    # 循环的读写文件
    while True:
        data = fr.read(1024)
        if not data:
            break   # 空表示文件结束
        fw.write(data)
    fr.close()
    fw.close()










