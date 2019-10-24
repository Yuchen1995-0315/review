"""
    使用容器思想，改造根据月份计算天的功能。
"""

year = int(input("请输入年份："))
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("月份有误")
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("29天")
    else:
        print("28天")
# elif month == 4 or month == 6 or month == 9 or month == 11:
elif month in (4,6,9,11):
    print("30天")
else:  # 1 3 5 7 8 10 12
    print("31天")

# 思路：将每月的天数，统一存入元组.
# days_of_month = (31,?,31,30,31,30,31,31,30,31,30,31)
# days_of_month[2]


