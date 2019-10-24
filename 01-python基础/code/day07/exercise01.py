# 练习1: 排列出所有扑克牌 13 * 4  --> 列表(52)
# 扑克牌的数字
list_number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# 扑克牌的花色
list_suit = ["红桃", "黑桃", "方片", "梅花"]

list_poker = [(number, suit) for number in list_number for suit in list_suit]
print(len(list_poker), list_poker)

# 练习2：排列出3个色子可以组成的所有数字6 * 6 × 6   --》 6**n
# 色子（1 -- 6）  6
list_result = []
for x in range(1, 7):
    for y in range(1, 7):
        for z in range(1, 7):
            list_result.append((x, y, z))

# list_result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(len(list_result), list_result)
