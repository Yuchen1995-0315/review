"""
    定义图形管理器
        1. 记录多种图形（圆形  矩形  三角 ....）
        2. 提供计算总面积的方法.
    满足：开闭原则
         依赖倒置
    测试：创建图形管理器，存储多个图形对象。
         通过图形管理器，调用计算总面积方法.
"""


# 17:15
class GraphicManager:
    def __init__(self):
        self.__list_graphic = []

    def add_graphic(self, target):
        self.__list_graphic.append(target)

    def calculate_total_area(self):
        sum_value = 0
        for item in self.__list_graphic:
            # 多态：
            # 调用的是图形计算面积方法
            # 执行的是圆形、矩形计算面积方法.
            sum_value += item.calculate_area()
        return sum_value

class Graphic:
    def calculate_area(self):
        """
            计算面积
        :return: 当天图形的面积
        """
        pass

class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2

class Rectanle(Graphic):
    def __init__(self, length=0, width=0):
        self.lenght = length
        self.width = width

    def calculate_area(self):
        return self.lenght * self.width

manager = GraphicManager()
manager.add_graphic(Circle(5))
manager.add_graphic(Rectanle(5, 6))
print(manager.calculate_total_area())
