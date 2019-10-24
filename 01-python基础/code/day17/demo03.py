"""
    lambda：匿名函数

    lambda 参数:方法体

    注意：
     方法体只能有一句话
     方法体不支持赋值语句

     15:25 上课
"""


# 普通方法
def fun01():
    print("fun01执行喽")


fun01()

# 无参数，无返回值
a = lambda: print("匿名方法执行喽")
a()


# 有参数，无返回值
def fun02(a, b, c):
    print("fun02执行喽", a, b, c)


fun02(1, 2, 3)

b = lambda a, b, c: print("匿名方法执行喽", a, b, c)
b(1, 2, 3)


# 有参数，有返回值
def fun03(a, b):
    return a > b


print(fun03(1, 2))

# lambda 方法体只能有一句话
c = lambda a, b: a > b
print(c(1, 2))


def fun04(obj):
    obj[0] = 100


list01 = [1]
fun04(list01)
print(list01)

# lambda 方法体不支持赋值语句
# d = lambda obj:obj[0] = 100








