"""
    练习1:
        1. 创建技能类(编号、名称、攻击力、持续时间、攻击间隔)
        2. 创建技能列表(不少于4种技能)
        3. 根据函数式编程思想完成以下功能：
            -- 功能1：定义查找编号是102的技能对象
            -- 功能2：定义查找名称是"辟邪剑法"的技能对象
                    (如果重名，只查找第一个)
            -- 功能3：定义查找持续时间大于10秒的单个技能对象
                    (如果有多个，只查找第一个)
        步骤：
            (1)先定义3个函数实现3个功能.
            (2)“封装”:拆分变化点、提取稳定的代码.
            (3)"继承":在稳定的代码中抽象变化(提取成参数)
            (4)"多态":将稳定的代码与变化的代码相结合.

    练习2：将find_single函数，移置IterableHelper类中
    练习3：
         根据函数式编程思想完成以下功能：
            -- 功能1：定义函数，查找编号大于101的技能数量
            -- 功能2：定义函数，查找攻击力在30-80之间的技能数量
        步骤：
            (1)先定义2个函数实现2个功能.
            (2)“封装”:拆分变化点、提取稳定的代码.
            (3)"继承":在稳定的代码中抽象变化(提取成参数)
            (4)"多态":将稳定的代码与变化的代码相结合.
            (5)将稳定的代码，移置IterableHelper类中命名为get_count
    练习4：
         根据函数式编程思想完成以下功能：
            -- 功能1：定义函数，计算所有技能的攻击力总合
            -- 功能2：定义函数，计算所有技能的持续时间总合
        步骤：
            (1)先定义2个函数实现2个功能.
            (2)“封装”:拆分变化点、提取稳定的代码.
            (3)"继承":在稳定的代码中抽象变化(提取成参数)
            (4)"多态":将稳定的代码与变化的代码相结合.
            (5)将稳定的代码，移置IterableHelper类中命名为sum
            (6)使用lambda调用IterableHelper类中的sum
    练习5：
         根据函数式编程思想完成以下功能：
            -- 功能1：定义函数，判断技能列表中是否存在功能力大于50的技能
            -- 功能2：定义函数，判断技能列表中是否存在持续时间为0的技能
        步骤：
            (5)将稳定的代码，移置IterableHelper类中命名为is_exists
            (6)使用lambda调用IterableHelper类中的is_exists
    练习6：
         根据函数式编程思想完成以下功能：
            -- 功能1：定义函数，获取技能列表中攻击力最强的技能
            -- 功能2：定义函数，获取技能列表中攻间隔最长的技能
        步骤：
            (5)将稳定的代码，移置IterableHelper类中命名为get_max
            (6)使用lambda调用IterableHelper类中的get_max
    练习7：
         根据函数式编程思想完成以下功能：
            -- 功能1：定义函数，获取技能列表中技能名称与攻击力
            -- 功能2：定义函数，获取技能列表中攻击力与攻击间隔与持续时间
        步骤：
            (5)将稳定的代码，移置IterableHelper类中命名为select
            (6)使用lambda调用IterableHelper类中的select
        思考：
            如何获取第一个/最后一个/后三个
    练习8：
        根据函数式编程思想完成以下功能：
            -- 功能1：定义函数，根据攻击力对技能列表进行升序排列
            -- 功能2：定义函数，根据持续时间对技能列表进行升序排列
        步骤：
            (5)将稳定的代码，移置IterableHelper类中命名为order_by
            (6)使用lambda调用IterableHelper类中的order_by
"""
from common.iterable_tools import IterableHelper


class Skill:
    def __init__(self, id, name, atk, duration, atk_interval):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration
        self.atk_interval = atk_interval

    # 对象 -->  str
    def __str__(self):
        return "%d -- %s -- %.1f -- %.1f --%.1f" % (self.id, self.name, self.atk, self.duration, self.atk_interval)

    # 重写对象比较逻辑
    # def __eq__(self, other):
    #     如果编号相同，就认为相同
    #     return self.id == other.id


list01 = [
    Skill(101, "葵花宝典", 50, 0, 0),
    Skill(102, "降龙十八掌", 80, 12, 1),
    Skill(103, "黯然销魂掌", 90, 15, 0.5),
    Skill(104, "辟邪剑法1", 70, 0, 0),
    Skill(104, "辟邪剑法2", 70, 0, 0),
]

print(list01[3] == list01[4])  # false

# 练习1
# (1)先定义3个函数实现3个功能.
def find_single01():
    for item in list01:
        if item.id == 102:
            return item


def find_single02():
    for item in list01:
        if item.name == "辟邪剑法":
            return item


def find_single03():
    for item in list01:
        if item.duration > 10:
            return item


# (2)“封装”:拆分变化点、提取稳定的代码.
def condition01(item):
    return item.id == 102


def condition02(item):
    return item.name == "辟邪剑法"


def condition03(item):
    return item.duration > 10

"""
# (3)"继承":在稳定的代码中抽象变化(提取成参数)
def find_single(func_condition):
    for item in list01:
        # if item.duration > 10:
        # if condition03(item):
        if func_condition(item):
            return item


# (4)"多态":将稳定的代码与变化的代码相结合.
print(find_single(condition02))
print(find_single(condition01))
"""

# 练习2
print(IterableHelper.find_single(list01,condition01))

# 练习3
def get_count01():
    count = 0
    for item in list01:
        if item.id > 101:
            count +=1
    return count

def get_count02():
    count = 0
    for item in list01:
        if 30 <= item.atk <= 80:
            count +=1
    return count

def condition01(item):
    return item.id > 101

def condition02(item):
    return 30 <= item.atk <= 80

"""
def get_count(func_condition):
    count = 0
    for item in list01:
        # if condition02(item):
        if func_condition(item):
            count +=1
    return count
"""

print(IterableHelper.get_count(list01,condition01))

print(IterableHelper.get_count(list01,lambda item:item.id > 101))

# 练习4：
"""
# -- 功能1：定义函数，计算所有技能的攻击力总合
def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.atk
    return sum_value
# -- 功能2：定义函数，计算所有技能的持续时间总合
def sum02():
    sum_value = 0
    for item in list01:
        sum_value += item.duration
    return sum_value

def handle01(item):
    return item.atk

def handle02(item):
    return  item.duration

def sum(func_handle):
    sum_value = 0
    for item in list01:
        # 先用
        sum_value += func_handle(item)
    return sum_value
"""
print(IterableHelper.sum(list01,lambda element: element.atk))


# 练习5:
print(IterableHelper.is_exists(list01,lambda item:item.atk > 50))

# 练习6：
print(IterableHelper.get_max(list01,lambda item:item.atk))

# 练习7：
result = IterableHelper.select(list01,lambda item:(item.name,item.atk))
# 生成器不支持 索引/切片查找  result[0]
# for item in result[-3:]:
#     print(item)

# 解决方案：
# 迭代生成器
# 将惰性操作（节省内存） --> 立即操作（灵活获取结果）
result = tuple(result)
print(result[-1])

# 作业：
IterableHelper.delete_all(list01,lambda item:item.duration ==0)
for item in list01:
    print(item)

