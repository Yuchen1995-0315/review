"""
    练习:创建技能类(技能名称,冷却时间,攻击力度,消耗法力)
                        0 -- 120  0 -- 200  -100 -- 100
        测试：创建一个技能，赋值不同数据,
"""


class SkillData:
    """
        技能数据类
    """

    def __init__(self, name="", cool_time=0, attack=0.0, cosp_sp=0):
        self.name = name
        self.cool_time = cool_time
        self.attack = attack
        self.cost_sp = cosp_sp

    @property
    def cool_time(self):
        return self.__cool_time

    @cool_time.setter
    def cool_time(self, value):
        if 0 <= value <= 120:
            self.__cool_time = value
        else:
            raise Exception("不在范围内")

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 0 <= value <= 200:
            self.__attack = value
        else:
            raise Exception("不在范围内")

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        if -100 <= value <= 100:
            self.__cost_sp = value
        else:
            raise Exception("不在范围内")


s01 = SkillData("九阳神功",500,100,50)

