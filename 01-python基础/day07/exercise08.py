# 练习:定义函数my_print(),调用３次.统计调用的次数.
count = 0


def my_print():
    global count
    count += 1


my_print()
my_print()
my_print()

print(count)
