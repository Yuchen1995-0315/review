"""
    continue
    练习：exercise04.py
"""

# 需求：累加1--100之间，能被5整除的数字.
# sum_value = 0
# for item in range(1, 101):
#     思想：满足条件累加
#     if item % 5 == 0:
#         sum_value += item
# print(sum_value)
sum_value = 0
for item in range(1, 101):
    # 思想：不满足条件跳过
    if item % 2 != 0:
        continue  # 跳过本次循环
    sum_value += item
print(sum_value)
