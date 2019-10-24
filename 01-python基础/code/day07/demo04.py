"""
    函数 -- 返回值（语法）
    练习:exercise04.py
"""


# 1. 函数返回值默认是None
def fun01():
    print("fun01执行喽")
    # return 100 # 返回数据
    # return # 返回    相当于 return None
    # 没有返回          相当于 return None


re = fun01()
print(re)


# 2. return 还可以退出函数
def fun02():
    print("fun02执行喽")
    return  # 退出函数
    print("fun02又执行喽")

fun02()
