"""
  笛卡尔积 全排列
  练习:exercise02
"""
import itertools

# 排列出所有扑克牌 13 * 4  --> 列表(52)
# 扑克牌的数字
list_number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# 扑克牌的花色
list_suit = ["红桃", "黑桃", "方片", "梅花"]

# list_poker = []
# for number in list_number:
#     for suit in list_suit:
#         list_poker.append((number, suit))
#
# print(len(list_poker), list_poker)

# for item in itertools.product(list_number,list_suit):
#     print(item)

result = tuple(itertools.product(list_number, list_suit))
print(len(result), result)

# 排列出3个色子可以组成的所有数字6 * 6 × 6   --》 6**n
# 色子（1 -- 6）  6
# list_result = []
# for x in range(1, 7):
#     for y in range(1, 7):
#         for z in range(1, 7):
#             list_result.append((x, y, z))
# print(len(list_result), list_result)

result = tuple(itertools.product(range(1, 7), repeat=3))
print(len(result), result)

# for item in itertools.product(range(1, 7),repeat=10):
#     print(item)



