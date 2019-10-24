"""
    隐藏数据 -- 通过property
    步骤：
        1. 在__init__方法中定义实例变量
        2. 使用@property修饰对象实例变量的读取方法
                注意:方法名与实例变量名相同
                     方法体返回私有变量
        3. 使用 @读取方法名.setter 修饰写入方法.
                注意:方法名与写入方法和实例变量名相同
                      方法体修改私有变量

"""
class Wife:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    # 创建property对象,绑定读取方法
    @property   #property(weight,None)
    # 读取方法
    def weight(self):
        return  self.__weight

    # 将写入方法也绑定到property对象中
    # 写入方法
    @weight.setter #
    def weight(self, value):
        if 20 <= value <= 200:
            self.__weight = value
        else:
            raise Exception("我不要")

    # weight = property(get_weight,set_weight)

w01 = Wife("芳芳", 40)
w01.weight = 45
print(w01.weight)

print(w01.__dict__)



