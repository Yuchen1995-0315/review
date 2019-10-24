"""
    隐藏数据 -- 通过property
    property 价值：将对实例变量的操作【拦截】下来,
                  转换给两个(读/写)方法
    练习:exercise02py
"""
class Wife:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight
        #self.set_weight(weight)
    # 写入方法
    def set_weight(self,value):
        if 20 <= value <=200:
            self.__weight = value
        else:
            raise Exception("我不要")
    # 读取方法
    def get_weight(self):
        return  self.__weight
    # 1. 创建类变量,覆盖实例变量（名称相同）
    # 2. 创建property对象 property(读取方法,写入方法)
    weight = property(get_weight,set_weight)

w01 = Wife("芳芳", 40)
# 3. 通过类变量直接修改数据
w01.weight = 45
print(w01.weight)

# w01.weight
# w01.__weight

# 通过方法修改数据
# w01.set_weight(45)
# 通过方法获取数据
# print(w01.get_weight())




print(w01.__dict__)



