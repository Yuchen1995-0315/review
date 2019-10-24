# 练习：猜数字1.0
# 程序产生1个1--100之间的随机数
# 在终端中重复猜测，直到猜对了为止
# 提示："大了"   "小了"   "猜对了，总共猜了?次"
import random  # 产生随机数的工具

# 产生随机数
random_number = random.randint(1, 100)
count = 0
while True:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break
