"""
(扩展)在控制台中录入一个秒，计算是几小时零几分钟零几秒钟.
"""
# 10:40
total_second = int(input("请输入总秒数："))
second = total_second % 60
hour = total_second // 60 // 60
minute = total_second // 60 % 60
# 在字符串中插入变量：
#  “...x...”      “..."+变量+"...”
print(str(hour) + "小时零" + str(minute) + "分钟零" + str(second) + "秒钟")
