"""
    列表推导式
    练习:exercise06.py
"""
# 需求1：将list01中的每个元素增加1以后，存入list02中。
list01 = [4, 54, 5, 65, 76, 89, 4]
# list02 = []
# for item in list01:
#     list02.append(item + 1)
list02 = [item + 1 for item in list01]
print(list02)

# 需求2：将list01中的所有偶数，存入list03中。
# list03 = []
# for item in list01:
#     if item % 2 == 0:
#         list03.append(item)
list03 = [item for item in list01 if item % 2 == 0]
print(list03)
