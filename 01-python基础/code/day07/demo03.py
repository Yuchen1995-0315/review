"""
    函数 -- 返回值（引入）
"""


# 需求: 定义函数，两个数值相加.

# 违反了"单一原则":一个函数只做一件事情.
# 函数定义者
# def add():
#     # 获取输入
#     number_one = float(input("请输入第一个数字："))
#     number_two = float(input("请输入第二个数字："))
#     # 逻辑处理
#     result = number_one + number_two
#     # 显示结果
#     print("结果是：%f" % result)

# 函数调用者
# add()

# 函数定义者
def add(number_one, number_two):
    # 逻辑处理
    result = number_one + number_two
    return result  # 返回结果


# 函数调用者
# 获取输入
# number_one = float(input("请输入第一个数字："))
# number_two = float(input("请输入第二个数字："))
re = add(50, 80)
print(re)
