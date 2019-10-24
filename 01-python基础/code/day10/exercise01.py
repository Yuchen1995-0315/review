"""
    练习：定义敌人类(数据：姓名，攻击力)
         限制攻击力范围:0 -- 100
"""
class Enemy:
    def __init__(self, name="", attack=0):
        self.name = name
        # 调用方法
        self.set_attack(attack)

    # 写入方法
    def set_attack(self, value):
        if 20 <= value <=200:
            # 修改私有数据
            self.__attack = value
        else:
            raise Exception("超过范围")

    # 读取方法
    def get_attack(self):
        # 返回私有数据
        return  self.__attack

e01 = Enemy("灭霸",500)
