"""
    多继承
        继承适用性：隔离变化
                  不作为代码复用的方式。
"""

# 同名方法解析顺序 MRO
class A:
    def m01(self):
        print("A -- m01")

class B(A):
    def m01(self):
        print("B -- m01")

class C(A):
    def m01(self):
        print("C -- m01")

class D(C,B):
    def m01(self):
        # super().m01()# 执行继承列表中第一个父类的同名方法
        # 通过类名调用同名实例方法
        B.m01(self)
        print("D -- m01")

d01 = D()
d01.m01()
#
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())





