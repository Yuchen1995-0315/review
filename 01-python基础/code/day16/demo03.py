"""
    yield -- 生成器函数
    练习:exercise06
    练习:exercise07
    练习:exercise08
"""

"""
class 生成器类:# 可迭代对象 + 迭代器对象
    def __iter__(self):
        return self
    
    def __next__(self):
        if 没有数据了：
            抛出异常
        return 数据

"""

def my_range(stop_value):
    start_value = 0
    while start_value < stop_value:
        # (3)每次执行到yield语句时返回数据，暂时离开。
        # (4)待下次调用__next__()方法时继续从离开处继续执行。
        yield start_value
        start_value += 1

# for item in my_range(3):
#     print(item)

# (1)创建生成器对象
generater = my_range(3)
iterator = generater.__iter__()
while True:
    try:
        # (2)调用迭代器对象的__next__()方法时才执行生成器函数
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break