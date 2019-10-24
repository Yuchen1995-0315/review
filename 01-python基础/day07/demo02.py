"""
    函数 -- 参数
"""

"""
# 代码的重复，是万恶之源.
print("直拳")
print("直拳")
print("勾拳")
print("临门一脚")
# ...............

print("直拳")
print("直拳")
print("勾拳")
print("临门一脚")
# ...............

print("直拳")
print("直拳")
print("勾拳")
print("临门一脚")
"""

# 定义函数
def attack01():
    """
        攻击
    """
    print("临门一脚")
    print("直拳")
    print("勾拳")
    print("直拳")

# 如果函数名称相同，则覆盖.
def attack02(count):# 形参:定义函数时使用的
    """
        攻击
    :param count: 攻击的次数,int类型
    """
    for i in range(count):
        print("临门一脚")
        print("直拳")
        print("勾拳")
        print("直拳")

# 调用函数
attack01()

attack02(3)# 实参：调用函数时使用的

attack02(2)

# 11:27 上课




