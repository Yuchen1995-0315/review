"""

"""

list01 = [4, 54, "65", 75, 8, "9", "b"]


# 需求1:找出所有偶数
def find01():
    for item in list01:
        if type(item) == int and item % 2 == 0:
            yield item


# 需求2:找出所有字符串
def find02():
    for item in list01:
        if type(item) == str:
            yield item


# 需求3:找出所有大于10的整数
def find03():
    for item in list01:
        if type(item) == int and item > 10:
            yield item


# "封装" : 拆分变化点
# "变化的"
def condition01(item):
    return type(item) == int and item % 2 == 0


def condition02(item):
    return type(item) == str


def condition03(item):
    return type(item) == int and item > 10

"""
# "继承"：抽象变化点 --> 统一变化 --> 隔离变化
# "不变的"  ----->  万能查找
def find(func_condition):
    for item in list01:
        # if condition01(item):
        if func_condition(item):
            yield item


# “多态”:调用父，执行子。
# 不变的 + 变化的
for item in find(condition03):
    print(item)
"""

from common.iterable_tools import IterableHelper

for item in IterableHelper.find_all(list01,condition01):
    print(item)






