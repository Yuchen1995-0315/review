"""
    练习3:参照下列代码，自定义MyRange类，实现相同效果.
    for item in range(10):
        print(item)

"""


class MyRnageIterator:
    def __init__(self, end_value):
        self.__begin_value = -1
        self.__end_value = end_value

    def __next__(self):
        # 0 1 2 3 8 9...   9
        if self.__begin_value == self.__end_value - 1:
            raise StopIteration
        self.__begin_value += 1
        return self.__begin_value

class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        return MyRnageIterator(self.__stop_value)

# 循环一次  调用一次next  返回一个结果
# 循环一次  调用一次next  返回一个结果
for item in MyRange(10):
    print(item)  # 0 1 2 ... 9


