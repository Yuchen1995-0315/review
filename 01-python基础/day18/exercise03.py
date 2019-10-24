import itertools

# 练习1： 计算在4张牌中排列4中的可能性
from common.iterable_tools import IterableHelper

tuple_poker = ("红桃3", "黑桃2", "梅花5", "大王")

list_result = list(itertools.permutations(tuple_poker, 4))
print(len(list_result), list_result)

# 练习2:"012345",可以组成多少个不重复的5位偶数
# list_result = list()
# print(len(list_result), list_result)
for item in filter(lambda item: item[0] != "0" and int(item[-1]) % 2 == 0, itertools.permutations("012345", 5)):
    # ('1', '0', '2', '3', '4') -->"10234" --> 10234
    print(int("".join(item)))
