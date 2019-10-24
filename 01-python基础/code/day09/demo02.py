"""
    实例成员
    练习:exercise02
"""
# 15:37 上课

class Wife01:

    def __init__(self, name):
        # 对象.变量名称
        self.name = name

    def print_self(self):
        print(self.name)


w01 = Wife01("丽丽")
w01.name = "莉莉"# 修改实例变量
w01.print_self()# 自动传递w01进入方法，给self赋值。

# 不建议：使用类名访问实例方法
# Wife01.print_self(w01)

# print(Wife01.name)

# 获取对象的所有实例变量(字典)
print(w01.__dict__)# {'name': '莉莉'}


# 实际开发不采用
# class Wife02:
#     pass

# w01 = Wife02()
# 对象.变量名称
# w01.name = "丽丽"
# print(w01.name)# "丽丽"


# 实际开发不采用
# class Wife03:
#     def __init__(self):
#         self.fun01()
#
#     def fun01(self):
#         # 对象.变量名称
#         self.name = "丽丽"
#
# w01 = Wife03()
# print(w01.name)# "丽丽"
