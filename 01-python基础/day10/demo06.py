"""
    封装 -- 设计角度

"""

# 需求:以面向对象的思想，描述以下情景:
#     老张开车去东北.
#
class Person:
    def __init__(self, name="",car = None):
        self.name = name
        # self.car = Car()# 创造我的车
        self.tool = car # 我可以使用不同交通工具

    def go_to(self,position):
        # Car().run()        # 去哪里都是一辆新车
        self.tool.run() #去哪里都是我的那辆车
        print("去东北")
    def go_home(self):
        self.tool.run()
        print("回家")
# 1. 确定需要调用的成员(实例)
# 2. 如果是实例成员，还需要确定创建对象的地点。
class Car:
    def run(self):
        print("走你...")

bm = Car()
lz = Person("老张",bm)
lz.go_to("东北")
lz.go_home()

# 17:05 上课












