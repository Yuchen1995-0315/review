"""
    外部嵌套作用域
"""


def fun01():
    a = 10
    def fun02():
        b = 20
        # print(a)  # 访问外部嵌套作用域中的变量
        # a = 30# 创建了局部变量a
        nonlocal a  # 声明外部嵌套作用域变量
        a = 30  # 再进行修改

    fun02()
    print(a)

fun01()
