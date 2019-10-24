"""
    继承复用：
        优势：直接使用，简单方便。
        缺点：紧耦合，父类变化直接影响所有后代.

    设计原则：组合复用
"""


class A:
    def __init__(self, a):
        self.a = a

    def a(self):
        print("A -- a")


class B(A):
    def __init__(self, p1, p2):
        super().__init__(p1)
        self.b = p2

    def b(self):
        print("B -- b")
        # 继承复用
        super().a()


b01 = B(1,2)
b01.b()
b01.a()
