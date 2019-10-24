"""
    继承 -- 数据
    练习:exercise02.py
"""


class Person:
    def __init__(self, name=""):
        self.name = name

class Student(Person):
    def __init__(self, name="", score=0):
        # 结论：创建子类对象，必须手动调用父类构造函数。
        # 调用父类构造函数 -->  创建父类的数据
        super().__init__(name)
        self.score = score

s01 = Student("张无忌", 100)
print(s01.score)
print(s01.name)


