"""
        场景：手雷爆炸了，可能伤害敌人、玩家生命.
        需求变化：还可能伤害房子、树、鸭子....
        要求：增加新事物，不影响手雷.
        体会：开闭原则
        画出架构设计图
"""

# 面向对象设计原则：
# 依赖倒置：调用抽象

class Granade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self,sufferer):
        print("手雷爆炸啦")
        sufferer.damage(self.atk)

class Sufferer:
    """
        抽象的受害者：隔离手雷与具体受害者的变化
    """
    def damage(self,value):
        pass

# ---------------------------
class Player(Sufferer):

    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        print("玩家受伤")
        self.hp -= value

class Enemy(Sufferer):

    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        print("敌人受伤啦")
        self.hp -= value

# 测试
g01 = Granade(50)
p01 = Player(500)
e01 = Enemy(100)

g01.explode(e01)
