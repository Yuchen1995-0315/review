"""
    类成员
"""


class ICBC:
    """
        工商银行
    """
    # 类变量：大家的信息 [饮水机]
    total_money = 1000000

    # 类方法
    @classmethod
    def print_total_money(cls):
        # print("总行的钱是:" ,ICBC.total_money)
        print("总行的钱是:", cls.total_money)

    def __init__(self, name, money):
        # 实例变量：某一个对象的信息   [杯子]
        self.money = money
        self.name = name
        # 创建支行时，从总行扣除相应的金额
        ICBC.total_money -= self.money


i01 = ICBC("天坛支行", 10000)
i02 = ICBC("陶然亭支行", 20000)
ICBC.print_total_money()  # 通过类名调用类方法，自动传递类名.
