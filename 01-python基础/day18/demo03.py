"""
    排列
        从n个元素中取出m个元素,并按照顺序进行排列.
        公式：n!  /  (n-m)!
"""
import itertools

# 7 个人 中取3个
# 7 * 6 * 5 * 4 * 3 * 2 * 1
# 4 * 3 * 2 * 1
tuple_person = ("男1号","男2号","男3号","女1号","女2号","女3号","女4号")
print(7 * 6 * 5)
result = tuple(itertools.permutations(tuple_person,3))
print(len(result),result)

