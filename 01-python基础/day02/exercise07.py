"""
    在终端中获取一个四位整数:1234
    计算每位相加和 1+2+3+4
"""
#16:50 上课
number = 1234
# # 方式1：
# # 个位
# unit01 = number % 10
# # 十位  1234 // 10 -->  123  % 10 --> 3
# unit02 = number // 10 % 10
# # 百位  1234 // 100 -->  12  % 10 --> 2
# unit03 = number // 100 % 10
# # 千位  1234 // 1000 --> 1
# unit04 = number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print("结果是：" + str(result))

# 方式2：
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print("结果是：" + str(result))
