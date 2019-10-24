"""
    创建老婆类(姓名、年龄、体重)
    创建老婆对象，直接print到终端。要求格式：臣妾xx,芳龄xx,体重xx。

    通过eval克隆老婆对象，修改其中一个老婆体重，查看另外一个老婆体重.
    体会：对象克隆技术.
"""
# 15:20
class Wife:
    def __init__(self, name="", age=0, weight=0):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return "臣妾%s,芳龄%d,体重%d。"%(self.name,self.age,self.weight)

    def __repr__(self):
        return "Wife('%s',%d,%d)"%(self.name,self.age,self.weight)

w01 = Wife("铁锤公主",28,200)
print(w01)

# 对象克隆
w02 = eval(repr(w01))
w01.weight = 180
print(w02)