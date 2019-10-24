"""
    python内置高阶函数
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

# 需求：找出编号大于102的所有技能
for item in IterableHelper.find_all(list01,lambda item:item.id > 102):
    print(item)

# 1.过滤器
for item in filter(lambda item:item.id > 102,list01):
    print(item)

# 需求：找出技能列表中所有技能编号和技能名称
for item in IterableHelper.select(list01,lambda item:(item.id,item.name)):
    print(item)

#2. 映射
for item in map(lambda item:(item.id,item.name),list01):
    print(item)

# 需求：找出技能列表中获取攻击力最大的技能
print(IterableHelper.get_max(list01,lambda item:item.atk))

# 3. 取最大值max  取最小 min
print(max(list01,key = lambda item:item.atk))


# 需求：对技能列表根据持续时间进行升序排列
# IterableHelper.order_by(list01,lambda item:item.duration)
# for item in list01:
#     print(item)

# IterableHelper.order_by_descending(list01,lambda item:item.duration)
# for item in list01:
#     print(item)

# 4. 排序
#      -- 返回排序后的结果，不改变原有数据。
#      -- 默认升序排列
#      -- 通过reverse=True 进行降序排列
# for item in sorted(list01,key =lambda item:item.duration):
#     print(item)
for item in sorted(list01,key =lambda item:item.duration,reverse=True):
    print(item)






