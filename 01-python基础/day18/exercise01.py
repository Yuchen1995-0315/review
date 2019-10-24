"""
    练习:
        使用内置高阶函数实现：
        1. ([1,1],[2,2,2],[3,3,3])
           获取元组中长度最大的列表
        2. 在老婆列表列表，获取所有名称与身高
        3. 在老婆列表中，获取所有体重大于50的老婆
        4. 对老婆列表，根据身高进行降序排列
        5. 获取所有身高大于1.6的老婆名称和身高.
"""


class Wife:
    def __init__(self, name="", weight=0.0, height=0.0):
        self.name = name
        self.weight = weight
        self.height = height

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Wife(" + self.name + ")"


list01 = [
    Wife("翠花", 60, 1.5),
    Wife("赵敏", 45, 1.7),
    Wife("铁扇公主", 55, 1.65),
    Wife("如花", 40, 1.6),
]

# 1.
tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tuple01, key=lambda item: len(item)))
# 2.
# 惰性操作 -->  立即操作
result = tuple(map(lambda item: (item.name, item.height), list01))
print(result[-2:])
# 3.
result = tuple(filter(lambda item: item.weight > 50, list01))
print(result)
# 4.
result = sorted(list01, key=lambda item: item.height, reverse=True)
print(len(result), result)
# 5.
for item in map(lambda item: (item.name, item.height), filter(lambda item: item.height > 1.6, list01)):
    print(item)

# 获取满足条件的所有人
# result = filter(lambda item:item.height > 1.6,list01)
# # 获取人的某些信息
# for item in map(lambda item:(item.name,item.height),result):
#     print(item)
