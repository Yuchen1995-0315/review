"""
练习：
编写一个程序，从终端输入一个单词，打印出该单词的解释，
如果输入的单词找不到则打印 “没有该单词”
"""

word = input("Word:")  # 输入要查找的单词

# 以读方式打开
f = open('dict.txt')

# 每次获取一行
for line in f:
    wd = line.split(' ',1)[0]
    # 如果遍历到的单词已经大于目标单词，就不必查找了
    if wd > word:
        print("没有找到该单词")
        break
    # 比较是不是输入的单词
    elif word == wd:
        print(line)
        # print(line.split(' ',1)[1].strip())
        break
else:
    print("没有该单词")

f.close()







