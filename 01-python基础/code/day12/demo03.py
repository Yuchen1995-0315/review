"""
    继承 -- 设计角度
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
        # 如果参数是汽车
        if type(vehicle) == Car:
            vehicle.run()
        # 否则如果是飞机
        elif type(vehicle) == Airplane:
            vehicle.fly()


class Car:
    def run(self):
        print("汽车行驶")


class Airplane:
    def fly(self):
        print("飞机天上飞")


c01 = Car()
lz = Person()

a01 = Airplane()
lz.go_to(a01)
