# 练习:
# 创建老婆类(姓名,体重,身高,年龄)
# 定义老婆列表
# -- 在老婆列表中，查找体重在30 - 50 之间的所有老婆对象
# -- 在老婆列表中，查找所有老婆的姓名与年龄.
# -- 在老婆列表中，查找姓名是"铁锤"的老婆对象
# 要求：定义函数实现
class Wife:
    def __init__(self, name="", weight=0.0, height=0.0, age=0):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age

list01 = [
    Wife("铁扇公主",50,1.6,27),
    Wife("白雪公主",40,1.7,23),
    Wife("铁锤",70,1.9,30),
    Wife("赵敏",35,1.5,27),
]

def find01():
    for item in list01:
        if 30 <= item.weight <= 50:
            yield item

def find02():
    for item in list01:
            yield (item.name,item.age)

def find03():
    for item in list01:
        if item.name == "铁锤":
            return item

for item in find01():
    print(item.name)

for item in find02():
    print(item)


tc = find03()
print(tc.name)








