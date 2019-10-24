# 练习:随机加法考试题
# 随机产生两个数字(1-10之间) 5   2
# 在终端中获取两个数字相加的结果  “请输入5+2=?”
# 如果回答正确加10分，错误减5分。
# 总共3道题，最后显示得分。
# 11:15

import random

score = 0
for item in range(3):#0 1 2
    random_number01 = random.randint(1,10)
    random_number02 = random.randint(1,10)
    input_number = int(input("请输入"+str(random_number01)+"+"+str(random_number02)+"=?"))
    if input_number == random_number01 + random_number02:
        score += 10
    else:
        score -= 5

print("得分是："+str(score))