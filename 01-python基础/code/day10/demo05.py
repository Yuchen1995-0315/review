"""
    属性
        价值：保护数据(加工数据,只读,只写)的行为，像操作变量一样方便.
    练习:exercise02
    15:30
"""

# 属性 标准写法
class Wife01:
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

w01 = Wife01(30)
w01.weight = 31
print(w01.weight)


# 属性 只读写法
class Wife02:
    def __init__(self, weight):
        # 创建对象时，创建只读的数据
        self.__weight = weight

    # 读取数据
    @property
    def weight(self):
        return self.__weight


w01 = Wife02(30)
# w01.weight = 31
print(w01.weight)


# 属性 只写 写法
class Wife03:
    def __init__(self, weight):
        self.weight = weight  # 执行 __set_weight 方法

    def __set_weight(self, value):
        self.__weight = value

    # property(读取方法，写入方法)
    weight = property(None, __set_weight)


w01 = Wife03(20)
print(w01.__dict__)
w01.weight = 30  # __set_weight
print(w01.__dict__)


# 私有成员 本质
class Wife04:
    def __init__(self, weight):
        # 实际将私有变量命名为：单下划线+类名+私有变量名
        #                  _Wife04__weight
        self.__weight = weight

w01 = Wife04(30)
# print(w01.__weight)
# 可以通过代码访问私有成员,但是违背了类设计者的用意.
# w01._Wife04__weight = 1000
print(w01.__dict__)









