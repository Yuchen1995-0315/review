# 张无忌教赵敏九阳神功
# 赵敏教张无忌玉女心经
# 张无忌工作挣了5000元
# 赵敏工作挣了10000元
# 测试：打印出每个人的技能、和存款.

class Person:
    def __init__(self, name=""):
        self.name = name
        self.skills = []
        self.money = 0

    def teach(self,other,skill):
        other.skills.append(skill)

    def work(self,value):
        self.money += value

zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach(zwj,"九阳神功")
zm.teach(zm,"玉女心经")

zwj.teach(zm,"九阳神功")
zm.teach(zwj,"玉女心经")
zwj.work(5000)
zm.work(10000)
print("张无忌：",zwj.money,zwj.skills)
print("赵敏：",zm.money,zm.skills)
