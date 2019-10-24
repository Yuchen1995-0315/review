"""
    自定义异常类
    练习:exercise04.py
"""


class WeightError(Exception):
    def __init__(self, message="", code="", id=0):
        # super().__init__()
        self.message = message
        self.code = code
        self.id = id


class Wife:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 20 <= value <= 200:
            self.__weight = value
        else:
            # 有意抛出异常
            # 传递的错误信息：错误原因,错误代码,错误编号,.....
            # raise Exception("体重超过范围")
            raise WeightError("体重超过范围", "if 20 <= value <= 200", 1001)


try:
    w01 = Wife("芳芳", 450)
except WeightError as e:
    print("错误编号是：", e.id)
    print("错误信息：", e.message)
    print("错误代码:", e.code)



