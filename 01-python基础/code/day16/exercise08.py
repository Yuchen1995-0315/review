# 练习：根据以下代码现象，自定义函数 my_zip.
# 17:05

list01 = ["张无忌", "张翠山", "张三丰"]
list02 = [101, 102, 103]

for itme in zip(list01, list02):
    print(itme)  # ('张无忌', 101)


def my_zip(iterable_target01, iterable_target02):
    for i in range(len(iterable_target01)):
        yield (iterable_target01[i], iterable_target02[i])


for itme in my_zip(list01, list02):
    print(itme)

list01 = ["张无忌", "张翠山", "张三丰"]
list02 = [101, 102]

for itme in zip(list01, list02, list02):
    print(itme)  # ('张无忌', 101)
