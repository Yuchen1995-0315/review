"""
    生成器表达式
    练习：exercise09.py
    练习：exercise10.py
"""
list01 = [2, 33, "a", 1.3, True, 2.5, False]

# 获取所有的小数
# result01 = []
# for item in list01:
#     if type(item) == float:
#         result01.append(item)
#
# print(result01)

# 列表推导式
result02 = [item for item in list01 if type(item) == float]
for item in result02:
    print(item)

# def get_floats():
#     for item in list01:
#         if type(item) == float:
#              yield item
#
# for item in get_floats():
#     print(item)

# 生成器表达式
result02 = (item for item in list01 if type(item) == float)
for item in result02:
    print(item)

# 请简述生成器与迭代器的关系.
# 答：生成器的本质就是迭代器，
# 生成器函数通过yield关键字将函数分解为多个部分，
# 每个部分就是一迭代器中的__next__方法.
# 生成器主要是延迟操作/惰性操作。
# 迭代器主要为了以一种方式获取可迭代对象中的元素.
