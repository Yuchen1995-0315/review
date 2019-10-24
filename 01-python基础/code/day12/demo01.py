"""
    继承 -- 语法
        财产：钱不用孩子挣，但是可以花.
        皇位：江山不用孩子打，但是可以坐.
        代码：子类不用写，但是可以用.
    练习:exercise01.py
"""


# 多个类具有相同成员，且都属于一种更大（宽泛）的概念 --> 继承
# 设计角度讲：先有子，再有父亲.
# 编码角度讲：先有父亲，再有子.

class Person:
    def say(self):
        print("说话")


class Student(Person):
    # def say(self):
    #     print("说话")

    def study(self):
        print("学习")


class Teacher(Person):
    # def say(self):
    #     print("说话")

    def teach(self):
        print("教学")


# 测试：
s01 = Student()
s01.say()
s01.study()

p01 = Person()
p01.say()

t01 = Teacher()
t01.say()
t01.teach()

# 内置函数

# 对象 -->  类型
# 学生对象 是 一个学生类型 True
print(isinstance(s01,Student))
# 学生对象 是 一个人类型 True
print(isinstance(s01,Person))
# 学生对象 是 一个老师类型False
print(isinstance(s01,Teacher))

# 类型 -->  类型
# 学生类型 是 一个人类型 True
print(issubclass(Student,Person))
# 学生类型 是 一个老师类型 False
print(issubclass(Student,Teacher))

# 人对象 是 一个学生类型 False
print(isinstance(p01,Student))
# 人类型 是 一个学生类型 False
print(issubclass(Person,Student))

# 10:25 上课





