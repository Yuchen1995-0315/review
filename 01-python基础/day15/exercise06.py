# 练习2:不适用for循环，获取字典中所有记录.
dict01 = {"a": 1, "b": 2, "c": 3}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
