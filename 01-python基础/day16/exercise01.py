"""
    练习: 迭代图形管理器
         体会（推导）自定义类如何参与for循环
"""

class GraphicIterator:
    """
         迭代器
    """

    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        if len(self.__target) - 1 == self.__index:
            raise StopIteration()
        # 返回下一个数据
        self.__index += 1
        return self.__target[self.__index]

class GraphicManager:
    """
        管理器
    """

    def __init__(self):
        self.__graphic = []

    def add_skill(self, str_graphic):
        self.__graphic.append(str_graphic)

    def __iter__(self):
        # 返回迭代器对象
        return GraphicIterator(self.__graphic)

manager = GraphicManager()
manager.add_skill("圆形")
manager.add_skill("三角形")
manager.add_skill("矩形")

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
