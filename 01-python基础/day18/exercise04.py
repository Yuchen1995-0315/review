import itertools

# 练习1： 计算在4张牌中组合2张中的可能性
tuple_poker = ("红桃3", "黑桃2", "梅花5", "大王")
# for item in itertools.combinations(tuple_poker,2):
#     print(item)

# 练习2：
# 药品调剂
# 分为3种药品，共取出100例粒，要求：没种必须都要有.
# 计算所有调剂方式
# 提示：思考共取出5粒如何实现
contents = 100
for item in itertools.combinations(range(1, contents), 2):
    # item 是 (1, 2) 板子的位置
    #     (2,4)
    for i in range(item[0]):
        print("A药品", end=" ")

    for i in range(item[1] - item[0]):
        print("B药品", end=" ")

    for i in range(contents - item[1]):
        print("C药品", end=" ")

    print()
