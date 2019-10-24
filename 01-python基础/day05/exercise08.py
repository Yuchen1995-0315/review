# 练习: 在终端中录入年月日，计算这是这一年的第几天.
# 2019 年  3 月 5 日
# 31 + 28 + 5

year = int(input("请输入年份："))
month = int(input("请输入月份："))  # 3
day = int(input("请输入天："))  # 5

if month <1 or month > 12:
    print("月份有误")
else:
    # 计算2月的天数
    day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    # 存储每月的天数
    days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # total_day = 0
    # for i in range(month - 1):
    #     total_day+= days_of_month[i]

    total_day = sum(days_of_month[:month - 1])

    total_day += day

    print(total_day)
