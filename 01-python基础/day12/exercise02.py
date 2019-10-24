"""
    练习:
        创建父类车(品牌，速度)
            子类电动车(电池容量,充电功率)
        创建父类对象，画出内存图。
        创建子类对象，画出内存图.
"""


class Car:
    def __init__(self, brand="", speed=0.0):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand="", speed=0.0, battery_capacity=0, charging_power=0):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


c01 = Car("宝马", 200)
e01 = Electrocar("比亚迪", 200, 15000, 220)
