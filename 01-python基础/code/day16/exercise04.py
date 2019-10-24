"""
      练习1：使用 yield 重构图形管理器/员工管理器
          调试程序，体会yield执行过程.


"""


class GraphicManager:
    """
        管理器
    """

    def __init__(self):
        self.__graphic = []

    def add_skill(self, str_graphic):
        self.__graphic.append(str_graphic)

    def __iter__(self):
        for itme in self.__graphic:
            # 返回数据
            yield itme  # 返回数据 暂时离开(再次调用__next__时回来)  [返回多个结果]
            # return item  返回数据并且退出方法 [返回一个结果]


manager = GraphicManager()
manager.add_skill("圆形")
manager.add_skill("三角形")
manager.add_skill("矩形")

for item in manager:
    print(item)