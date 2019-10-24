"""
    迭代器
    10:10
    练习：exercise01.py
        exercise02.py
        exercise03.py
"""


class SkillIterator:
    """
        技能迭代器
    """

    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        if len(self.__target) - 1 == self.__index:
            raise StopIteration()
        # 返回下一个数据
        self.__index += 1
        return self.__target[self.__index]


class SkillManager:
    """
        技能管理器
    """

    def __init__(self):
        self.__skills = []

    def add_skill(self, str_skill):
        self.__skills.append(str_skill)

    def __iter__(self):
        # 返回迭代器对象
        return SkillIterator(self.__skills)

manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("九阴白骨爪")
manager.add_skill("化骨绵掌")

# for item in manager:
#     print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
