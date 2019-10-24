# 练习: 定义敌人类(姓名，攻击力)，要求限制攻击力范围在0--50之间
#       如果不在范围内，抛出异常，
#       传递3个错误信息(错误编号/错误信息/错误代码)
class AtkError(Exception):
    def __init__(self, id=0, message="", code=""):
        super().__init__(message)
        self.error_id = id
        self.error_message = message
        self.error_code = code


class Enemy:
    def __init__(self, name="", atk=0):
        self.name = name
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 50:
            self.__atk = value
        else:
            raise AtkError(101, "攻击力不在范围内", "if 0<=value<=50")
            # 如果想偷偷懒，也可以尝试使用Exception传递多个错误信息.
            # raise Exception("a","b","c")


# try:
#     e01 = Enemy("灭霸", 100)
# except AtkError as e:
#     print(e.error_message)

try:
    e01 = Enemy("灭霸", 100)
except Exception as e:
    print(e.args[0])
    print(e.args[1])
    print(e.args[2])
# 17:05
