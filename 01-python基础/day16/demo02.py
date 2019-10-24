"""
    迭代器  --> yield
    练习1：
        使用 yield 重构图形管理器/员工管理器
        调试程序，体会yield执行过程.
        exercise04
    练习2：
        使用 yield 重构MyRange.
        调试程序，体会yield执行过程.
"""

class SkillManager:
    """
        技能管理器
    """

    def __init__(self):
        self.__skills = []

    def add_skill(self, str_skill):
        self.__skills.append(str_skill)

    def __iter__(self):
        # 自动生成迭代器代码
        # 大致生成过程：
        # 1. 将yield关键字以前的代码放到__next__方法中。
        # 2. 将yield关键字以后的数据作为__next__方法返回值
        # print("准备数据")
        # yield "九阳神功"
        #
        # print("准备数据")
        # yield "九阴白骨爪"
        #
        # print("准备数据")
        # yield "化骨绵掌"

        for item in self.__skills:
            yield item

manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("九阴白骨爪")
manager.add_skill("化骨绵掌")

# for item in manager:
#     print(item)

# 调用__iter__方法不执行
iterator = manager.__iter__()
while True:
    try:
        # 调用__next__方法,执行__iter__方法语句
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
