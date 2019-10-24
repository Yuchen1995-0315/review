"""
    函数参数
        形式参数
    练习:exercise01.py
    练习:demo02.py
    练习:exercise03.py
    练习:exercise04.py
    练习:exercise05.py
"""


# 1. 位置形参
def fun01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 2. 默认参数:实参可以不传递(必须从右向左依次存在)
def fun02(p1="", p2=0, p3=0.0):
    print(p1)
    print(p2)
    print(p3)


fun02("a", 2, 3)
fun02("a")
fun02(1)
fun02()
# 关键字实参 + 默认参数：可以随意指定形参进行传递。
fun02(p3=2)


# 3. 星号元组形参：让位置实参数量无限(最多一个).  合
def fun03(*args):
    print(args)


fun03()
fun03(1)
fun03(4, 345, 54, 56, 67, 7)


# fun03(a = 1,b =2)  错误

def fun04(p1, *args):
    print(p1)
    print(args)


fun04(1)
fun04(1, 34, 4, 5)


# 4. 命名关键字形参:在星号元组形参后面的形参.
#                 在星号后面的形参.
#             作用:要求调用者必须使用关键字实参.
def fun05(*args, p1):
    print(p1)
    print(args)


fun05(324, 23, 4, 45, 46, p1=7)


def fun06(p1, *, p2):
    print(p1)
    print(p2)


fun06(1, p2=2)


# 5. 双星号字典形参：让关键字实参数量无限(最多一个).  合
def fun07(**kwargs):
    print(kwargs)# 函数内部　得到的是字典对象

fun07(a=1, b=2, c=3)








