# 练习：在终端中录入一个分数，显示等级.
# 不及格  及格  良好  优秀  输入有误(范围不在0--100之间)

score = float(input("请输入成绩："))
# if score >= 90 and score <= 100:
#     print("优秀")
# elif score >= 80 and score < 90:
#     print("良好")
# elif score >= 60 and score < 80:
#     print("及格")
# elif score >= 0 and score < 60:
#     print("不及格")
# else:
#     print("输入有误")

# if 90 <= score <= 100:
#     print("优秀")
# elif 80 <= score < 90:
#     print("良好")
# elif 60 <= score < 80:
#     print("及格")
# elif 0 <= score < 60:
#     print("不及格")
# else:
#     print("输入有误")

# score == 85

if score > 100 or score <0:
    print("输入有误")
elif 90 <= score:
    print("优秀")
elif 80 <= score:
    print("良好")
elif 60 <= score:
    print("及格")
else:
    print("不及格")



