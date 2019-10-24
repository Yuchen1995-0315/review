# 练习: 根据以下代码现象，自定义函数 my_enumerate.
list01 = [4, 54, 5, 6, 7, 8, 9]

# 如果希望遍历可迭代对象时，具有索引，使用enumeraten内置生成器
for item in enumerate(list01):
    print(item)  # (索引,元素)

for index, element in enumerate(list01):
    print(index, element)  # (索引,元素)


def my_enumerate(iterable_target):
    index = 0
    for item in iterable_target:
        yield (index, item)
        index += 1


for index, element in my_enumerate(list01):
    print(index, element)  # (索引,元素)

dict01 = {"a": "A", "b": "B"}
for index, key in enumerate(dict01):
    print(index, key, dict01[key])
