"""
    时间模块 time
    10:10
    练习：exercise01 / 02
"""
import time

# 1. 获取当前时间戳（从1970年1月1日到现在经过的秒数）
# 1568856576.399807
print(time.time())

# 2. 获取当前时间元组
# tm_year=2019, tm_mon=9, tm_mday=19, tm_hour=9, tm_min=33, tm_sec=31, tm_wday=3, tm_yday=262, tm_isdst=0
print(time.localtime())

# 3. 时间戳 --> 时间元组
time_tuple = time.localtime(1568856576.399807)
print(time_tuple)
print("年份：",time_tuple[0])
print("星期",time_tuple[6] + 1)

# 4. 时间元组 --> 时间戳
print(time.mktime(time_tuple))

# 5. 时间元组 --> str
print(time.strftime("%y/%m/%d %H:%M:%S",time_tuple))
print(time.strftime("%Y/%m/%d %H:%M:%S",time_tuple))

# 6. str --> 时间元组
print(time.strptime("19/09/19 09:29:36","%y/%m/%d %H:%M:%S"))










