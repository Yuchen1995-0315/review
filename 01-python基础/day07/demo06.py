"""
    作用域 -- 局部/全局
    练习:exercise08
"""
# 全局作用域：整个.py文件(在函数外)
# 全局变量
g01 = "a"


def fun01():
    # 局部作用域：函数体内部
    # 局部变量
    a = 100
    print(a)
    # 只能读取全局变量
    print(g01)
    print(g02)


g02 = "b"
fun01()

def fun02():
    # 不行修改全局变量
    # g01 ="A"

    # 通过global声明全局变量g01
    global g01
    g01 = "A"

fun02()
print(g01)


