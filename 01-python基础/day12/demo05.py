"""
    继承时，子类可以super()调用方法.
"""


class Granade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self, sufferer):
        print("手雷爆炸啦")
        sufferer.damage(self.atk)

class Sufferer:
    """
        抽象的受害者：隔离手雷与具体受害者的变化
    """

    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        self.hp -= value

# ---------------------------
class Player(Sufferer):

    def damage(self, value):
        print("玩家受伤")  # 个性
        super().damage(value)  # 共性

class Enemy(Sufferer):

    def damage(self, value):
        print("敌人受伤啦")  # 个性
        super().damage(value)  # 共性

# 测试
g01 = Granade(50)
p01 = Player(500)
e01 = Enemy(100)

g01.explode(e01)
print(e01.hp)
