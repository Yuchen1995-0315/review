
# 练习1:使用for循环原理(迭代思想),获取元组中所有元素.
tuple01 = (4,4,5,6,7,9)
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break


