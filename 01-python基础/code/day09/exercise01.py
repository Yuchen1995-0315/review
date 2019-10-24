"""
    谁？　　　　　　　干嘛？
    类　－－> 对象   方法
    练习：
        创建狗类
            数据
                爱称
                品种
                年龄
            行为
                玩
                坐下

        创建２条狗,分别让它们坐下／玩.
        画出内存图
"""


class Dog:
    """
        抽象的狗类
    """

    def __init__(self, name, breed="野狗", age=0):
        self.pet_name = name
        self.breed = breed
        self.age = age

    def play(self):
        print(self.pet_name + "在玩耍")

    def sit_down(self):
        print(self.pet_name + "坐下了")


d01 = Dog("米咻", "拉布拉多", 4)
d01.play()
d01.sit_down()

d02 = Dog("黑米", "拉布拉多", 2)
d02.play()
d02.sit_down()

# 一个函数，如何找到相应的对象?
# 通过函数的self
