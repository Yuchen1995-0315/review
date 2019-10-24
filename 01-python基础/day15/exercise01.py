"""
    练习1：定义函数,根据年月日计算星期数.
           星期一
           星期二
           ....
           星期日
"""
import time


def get_week(year, month, day):
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    # print(time_tuple[6])# 3 --> 星期四
    # if time_tuple[6] == 0:
    #     return "星期一"
    # if time_tuple[6] == 1:
    #     return "星期二"
    tuple_weeks = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_weeks[time_tuple[6]]

print(get_week(2019, 9, 19))

