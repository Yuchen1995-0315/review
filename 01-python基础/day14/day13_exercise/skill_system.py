"""
    技能系统
    11:25
"""


class SkillImpactEffect:
    """
        技能影响效果:负责统一/抽象具体影响效果.
                  隔离技能释放器与具体影响效果的变化
    """

    def impact(self):
        pass


class DamageEffect(SkillImpactEffect):
    """
        伤害效果
    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, value=0, time=0.0):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%.1f防御力,持续时间%.1f" % (self.value, self.time))


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕
    """

    def __init__(self, time=0.0):
        self.time = time

    def impact(self):
        print("眩晕持续时间%.1f" % self.time)


class SkillDeployer:
    """
        技能释放器:生成技能（执行当前技能的各种影响效果）
    """

    def __init__(self, name=""):
        self.name = name
        # 读取配置文件
        self.__dict_skill_config = self.__load_config_file()
        # 创建各种影响效果对象
        self.__list_effect_object = self.__create_effect_objects()

    def __load_config_file(self):
        return {
            "韦陀杵": ["DamageEffect(50)"],
            "祝融掌": ["DamageEffect(80)", "LowerDeffenseEffect(0.9,2)"],
            "降龙十八掌": ["DamageEffect(150)", "LowerDeffenseEffect(0.2,3)", "DizzinessEffect(30)"],
        }

    def __create_effect_objects(self):
        # self.name --> self.__dict_skill_config --> [各种影响效果名称]
        list_effect_name = self.__dict_skill_config[self.name]
        # list_object = []
        # for item in list_effect_name:
        #     # itme --> "DamageEffect(50)" --> DamageEffect(50)
        #     effect_object = eval(item)
        #     list_object.append(effect_object)
        # return list_object
        return [eval(item) for item in list_effect_name]

    def generate_skill(self):
        """
            生成技能(执行各种影响效果)
        """
        print(self.name + "技能释放啦")
        for item in self.__list_effect_object:
            item.impact()


zrz = SkillDeployer("祝融掌")
zrz.generate_skill()
zrz.generate_skill()

xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()


# 练习1：通过调试，写出程序执行过程。
# 练习2：通过理论，写出技能系统体现的三大特征与六大原则。
# ....
# 练习3：指出技能系统的优势。
#  1) 外部一个需求变化，内部一个类发生改变.     [封装 - 单一职责]
#        伤害算法        DamageEffect
#  2) 如果增加新影响效果，只需要增加新类，无需改变其他代码.  【开闭原则】
#  3) 如果某个技能影响效果变化(减少/增加)，只需要修改配置文件，无需改变代码.【依赖注入】













