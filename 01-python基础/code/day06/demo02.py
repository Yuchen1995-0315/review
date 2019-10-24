"""
    字典推导式
    练习：exercise04.py
"""
# 需求：range(10)    key:0--9   value: 键的平方
# dict01 = {}
# for item in range(10):
#     dict01[item] = item ** 2

dict01 = {item: item ** 2 for item in range(10)}
print(dict01)

# 需求：range(10)    key:0--9   value: 键的平方
#      2 < key < 8
dict01 = {item: item ** 2 for item in range(10) if 2 <item<8}
print(dict01)

