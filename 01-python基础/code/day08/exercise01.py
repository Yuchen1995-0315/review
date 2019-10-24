# 练习:定义函数，根据分钟，小时，秒计算总秒数.
# 测试：1分钟，1小时，1秒  --> ?
# 测试：2分钟 --> ?
# 测试：3小时 --> ?
# 测试：2分钟,5秒 --> ?
# 测试：3分钟,2秒 --> ?
def get_total_second(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second

print(get_total_second(1, 1, 1))
print(get_total_second(minute=2))
print(get_total_second(hour=3))
print(get_total_second(3))
print(get_total_second(minute=2, second=5))
print(get_total_second(hour=3, second=2))
print(get_total_second(3, second=2))
