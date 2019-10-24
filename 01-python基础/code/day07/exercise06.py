"""
   练习3: 将day05/exercise07功能,封装到函数中。

    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    if month < 1 or month > 12:
        print("月份有误")
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("29天")
        else:
            print("28天")
    elif month in (4,6,9,11):
        print("30天")
    else:
        print("31天")
"""

def is_leap_year(year):
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# 返回值类型应该是整数(天)
# 返回值类型应该是一种(可以返回不可能的数值)
def calculate_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        # if is_leap_year(year):
        #     return 29
        # else:
        #     return 28
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30

    return 31

print(calculate_day_by_month(2019, 16))
