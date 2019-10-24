"""
    运算符重载（重写）
    适用性：希望自定义类创建的对象，使用python运算符.
    重点：__eq__    __str__    __repr__
"""
# 17:00
class Vector1:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "向量的分量是:" + str(self.x)

    # 算数运算符：自身类型 + 其他类型
    def __add__(self, other):
        if type(other) == Vector1:
            return Vector1(self.x + other.x)
        else:
            return Vector1(self.x + other)

    # 反向算数运算符: 其他类型 + 自身类型
    def __radd__(self, other):
        return self.__add__(other)

    # 复合运算符：如果不存在，默认调用__add__,返回新对象.
    #           如果存在，往往会在__iadd__中返回自身对象.
    def __iadd__(self, other):
        if type(other) == Vector1:
            self.x += other.x
        else:
            self.x += other
        return self

    # 比较运算符：如果不存在，默认使用地址进行比较。
    #           所以即使对象各个数据相同，也会判断为false.
    def __eq__(self, other):
        return self.x == other.x


v01 = Vector1(20)
v02 = Vector1(20)

# 1.算数运算符
print(v01 + v02)  # v01.__add__(v02)
# 练习1:自行选择另外2种运算符重载实现.

# 2.反向算数运算符
# print(v01 + 20.5)# v01.__add__(20.5)
print(20.5 + v01)  # v01.__radd__(20.5)
print(v01 + 20.6)
# 练习2:自行选择另外2种反向算数运算符重载实现.

# 3. 复合算数运算符
print(id(v01))
v01 += 2
print(id(v01))
print(v01)

# list01 = [1,2,3]
# print(id(list01))
# list01 += [4]
# print(id(list01))
# print(list01)
# 练习3:自行选择另外2种复合运算符重载实现.

# 4. 比较运算符
print(v01 == v02)
# 练习4:自行选择另外2种比较运算符重载实现.