# 练习1:在列表中获取所有整数,并计算它的平方.
# 练习2:在列表中获取所有大于10的小数.
# 要求：使用列表推导式，生成器表达式完成.
# 通过调试，体会差异.

list01 = [43.9, 54, "b", 5, 6.5, "a", 67, 7.6, 8.8, 9]
# 练习1
result01 = [item ** 2 for item in list01 if type(item) == int]
for item in result01:
    print(item)

result02 = (item ** 2 for item in list01 if type(item) == int)
for item in result02:
    print(item)

# 练习2
result01 = [item for item in list01 if type(item) == float and item > 10]
for item in result01:
    print(item)

result02 = (item for item in list01 if type(item) == int and item > 10)
for item in result02:
    print(item)
