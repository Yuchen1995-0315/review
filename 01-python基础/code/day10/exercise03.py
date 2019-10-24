"""
 需求:以面向对象的思想，描述以下情景:
      小明  在 银行   取钱.
      钱多了  钱少了
      分析：小明用银行的取钱功能。


"""


class Person:
    def __init__(self, name="", money=0):
        self.name = name
        self.money = money


class Bank:
    def __init__(self, money=0):
        self.money = money

    def draw_money(self, value, other):
        print("取钱啦")
        self.money -= value
        # 不应该是取钱时创造了人
        # Person("小明",0).money += value
        other.money += value
        print("%s的钱多啦." % other.name)


xm = Person("小明", 0)
yh = Bank(100000)
# 调用银行取钱功能,传递小明.
yh.draw_money(5000, xm)

