# 练习1:使用列表推导式生成1--50之间能被3 或者 5 整除的数字.
# result01 = []
# for item in range(1,51):
#     if item % 3 == 0 or item % 5 == 0:
#         result01.append(item)

result01 = [item for item in range(1,51) if item % 3 == 0 or item % 5 == 0]

# 练习2:使用列表推导式生成5 -- 20 之间数字的平方.
result02 = [item ** 2 for item in range(5,21)]
print(result01)
print(result02)

# 16:50