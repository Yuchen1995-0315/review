"""
    玩家攻击(攻击力)敌人，敌人受伤(减血)后可能死亡(播放死亡动画)
    敌人攻击(攻击力)玩家，玩家受伤(减血,碎屏)后可能死亡(游戏结束)
"""
# 分析三个设计案例
# 10:20 上课

class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("敌人受伤减血啦")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("播放死亡动画")

    def attack(self, target):
        print("敌人发起了攻击")
        target.damage(self.atk)


class Player:
    def __init__(self, hp=0, atk=0):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print("玩家发起了攻击")
        # Enemy(100).damage(self.atk)
        target.damage(self.atk)

    def damage(self, value):
        print("玩家受伤减血，碎屏。")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("游戏结束")


e01 = Enemy(1000, 100)
p01 = Player(5000, 500)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)
