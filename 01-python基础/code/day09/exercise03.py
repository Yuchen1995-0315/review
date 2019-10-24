"""
    练习: 对象计数器
          用过类变量，记录一个类创建对象(__init__)的次数.
          要求：定义类方法，打印类变量.
               画出内存图.
          测试：创建3个对象，然后调用类方法.
"""


class Dog:
    count = 0

    def __init__(self):
        Dog.count += 1

    @classmethod
    def print_count(cls):
        print("总共创建了%d个对象" % cls.count)

Dog()
Dog()
Dog()
Dog.print_count()
