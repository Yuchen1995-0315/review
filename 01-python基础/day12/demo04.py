"""
    继承 -- 设计角度
    15:20
"""


# 面向对象设计原则：
#   开闭原则：开放       关闭
#        允许增加新功能  不改变(增加/删除/修改)"以前"的代码

# 老张开车去东北
# 需求变化：火车、飞机、坦克...
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("去东北")
        # 调用抽象的交通工具，而不调用更具体的汽车、飞机.
        vehicle.transport()

class Vehicle:
    """
        抽象的 交通工具
    """
    def transport(self):
        pass

# -----------------------------------------------------

class Car(Vehicle):
    def transport(self):
        print("汽车行驶")


class Airplane(Vehicle):

    # ctrl + o
    # 重写(覆盖)
    def transport(self):
        print("飞机天上飞")


c01 = Car()
lz = Person()

a01 = Airplane()
lz.go_to(c01)
