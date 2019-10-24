"""
    练习:
        创建三个类:
            狗类(跑)
            鸟类(飞)
            动物(吃)
        创建父类与子类对象，调用相关方法.体会 子类复用父类方法.
        体会isinstance 与 issubclass 的异同.
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")


class Bird:
    def fly(self):
        print("飞")


d01 = Dog()
d01.run()
d01.eat()

a01 = Animal()
a01.eat()

# 狗对象 是 是一种 动物类型
print(isinstance(d01, Animal))
# 狗类型 是一种 动物类型
print(issubclass(Dog, Animal))
# 狗对象 是 是一种 狗类型
print(isinstance(d01, Dog))

# 狗对象 是 狗类型 True
print(type(d01) == Dog)
# 狗对象 是 动物类型  False
print(type(d01) == Animal)
