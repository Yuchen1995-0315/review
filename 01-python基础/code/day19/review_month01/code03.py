"""
    11:30
    第三门课：python核心
        程序结构：
            为什么要有模块和包？ --- 代码结构清晰
            各种导入方式
            main.py的价值 --- 主模块不会生成pyc文件
        异常处理：
            异常现象：不再向下执行，而是不断返回给调用者，直到程序最外层或者try.
            处理目的：异常现象 --> 正常现象.
            处理手段：
                try:
                    可能出错的代码
                except 错误类型1 as 变量名：
                    处理逻辑,通过变量名可以访问错误对象
                except 错误类型2 as 变量名：
                    处理逻辑,通过变量名可以访问错误对象
                else:
                    不出错的逻辑

                try:
                    可能出错的代码
                finally:
                    一定执行的逻辑
                注意：没有处理异常
        迭代 iter
            可迭代对象 iterable：__iter__() -- 可以被for
            迭代器 iterator:__next__() -- 可以返回数据
            架构图

        生成器
            本质：迭代器 + 可迭代对象()
            生成器函数：
                def 函数名():
                    ...
                    yield 数据
                    ...

                通常使用for获取数据
                也可以通过__next__获取数据，通过send发送数据
                通过tuple(生成器),将惰性操作变为立即操作
            价值：循环一次，计算一次，返回一次,
                  节省内存

        函数式编程
            函数作为参数
                参数：数值、列表、自定义对象 --> 传递数据
                参数：函数--> 传递逻辑/算法/行为
                IterableHelper类 --> "万能"

            函数作为返回值
                闭包 --> 装饰器（拦截）

"""
# 快捷键：iter + 回车 + Tab
for char in "abcd":
    print(char)


def fun01():
    for i in range(10):
        value = yield i
        print(value)  # "偶数"  None

generate = fun01()
for item in generate:  # generate.__next__()
    print(item)
    if item % 2 == 0:
        # 在迭代过程中给生成器发送信息
        generate.send("偶数")
