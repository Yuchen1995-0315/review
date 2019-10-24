"""
    隐藏数据 -- 通过方法(不采用)
            本质：两个方法，保护一个私有数据.
    练习:exercise01.py
"""


class Wife:
    def __init__(self, name="", weight=0):
        self.name = name
        # 如果不隐藏数据，外部可以任意操作.
        # self.weight = weight
        self.set_weight(weight)

    # 写入方法
    def set_weight(self,value):
        if 20 <= value <=200:
            self.__weight = value
        else:
            raise Exception("我不要")

    # 读取方法
    def get_weight(self):
        return  self.__weight


w01 = Wife("芳芳", 40)
# w01.weight
# w01.__weight

# 通过方法修改数据
w01.set_weight(45)
# 通过方法获取数据
print(w01.get_weight())

print(w01.__dict__)



