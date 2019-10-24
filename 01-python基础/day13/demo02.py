"""
    组合复用：
        通过变量调用，而不是通过继承使用.


    设计原则：组合复用
"""
class A2:
    def a(self):
        print("A -- a2")

class A:
    def a(self):
        print("A -- a")

class B:
    def __init__(self,p1):
        self.a_object = p1# 组合关系

    def b(self):
        print("B -- b")
        self.a_object.a()

# 如果传递其他对象，等同于修改了b方法的行为，还不影响b方法.
b01 = B(A2())
b01.b()
