# 练习：
# 在终端中获取一个四位整数，计算每位相加和.
# “1234” --> “1”  --> 1
#        --> “2”  --> 2

str_number = input("请输入整数：")
result = 0
for item in str_number:
    result += int(item)
print(result)

# 三板斧：调试、 内存图、..
# 10:15 上课