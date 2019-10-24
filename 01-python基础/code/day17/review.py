"""
    复习
        迭代 iter
            可迭代对象iterable:包含__iter__()方法
                作用：能够被for

            迭代器对象iterator:包含__next__()方法
                作用：以【一种】方式获取容器【多种数据结构】的下一个元素
        生成器
            可迭代对象 + 迭代器对象
            生成器函数
                def 函数名称():
                    ...
                    yield 数据
                    ...

                for item in 函数名称():
                    itme 存储的是yield后面的数据

            生成器表达式
                结果 = (对item处理 for item in 可迭代对象 if 条件)
                for item in 结果:
                    ...
"""
str01 = "大家好，才是真的好."
list01 = [23,34,4,5]
# for item in str01:
#     print(item)

# 书写for循环的快捷键： iter + 回车  +tab




