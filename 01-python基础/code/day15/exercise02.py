# 练习：定义函数,根据生日(年月日),计算活了多天.
#  公式：现在 - 生日
import time
# 11:25

def life_days(year, month, day):
    # year,month,day --> 时间元组
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    life_second = time.time() - time.mktime(time_tuple)
    return life_second / 60 / 60 // 24


print("%d" % life_days(1999, 1, 1))
