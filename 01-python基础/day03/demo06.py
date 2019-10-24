"""
    while 条件:
        循环体
    else:
        条件不满足，才执行的代码.
"""

# 需求：3次

import random  # 产生随机数的工具

# 产生随机数
random_number = random.randint(1, 100)
print(random_number)

count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break
else:# 只有猜错次数超过3次，才会执行else语句。(猜对了，不执行)
    print("失败啦")
# 价值：判断循环结束，是因为不满足条件，还是循环体中的break,
