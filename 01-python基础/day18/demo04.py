"""
    组合
        从n个元素中取出m个元素
        不考虑顺序的排列
    练习：exercise04.py
"""

import itertools

# 7 个人 中取3个
tuple_person = ("男1号", "男2号", "男3号", "女1号", "女2号", "女3号", "女4号")
result = list(itertools.combinations(tuple_person, 3))
print(len(result), result)
