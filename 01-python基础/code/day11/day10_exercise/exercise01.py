"""
创建手机类(名称, 价格,  重量,大小(宽  ,  高, 厚度))
               0-15000  2-10   2-10   2-20  0.1 - 2
   要求：限制数据不超过以上范围
"""


class MobilePhone:
    """
        移动电话
    """

    def __init__(self, name="", price=0.0, weight=0, size=()):
        self.name = name
        self.price = price
        self.weight = weight
        self.size = size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if 0 <= value <= 15000:
            self.__price = value
        else:
            raise Exception("数据不在范围")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 2 <= value <= 10:
            self.__weight = value
        else:
            raise Exception("数据不在范围")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if 2 <= value[0] <= 10 and 2 <= value[1] <= 20 and 0.1 <= value[2] <= 2:
            self.__size = value
        else:
            raise Exception("数据不在范围")


m01 = MobilePhone("三星手机", 5000, 5, (5, 10, 0.8))
print(m01.name)
print(m01.price)
print(m01.weight)
print(m01.size)
