"""
    练习:在exercise01.py中使用三种导入方式，
        调用module02模块中的三个方法(fun01,fun02,fun03).
        体会三种导入方式区别
"""

# 方式1
"""
import module02
module02.fun01()

# m01 = module02.MyClass()
# m01.fun02()
module02.MyClass().fun02()
module02.MyClass.fun03()
"""
# 方式2
"""
from module02 import fun01,MyClass
fun01()
MyClass().fun02()
MyClass.fun03()
"""
# 方式3
from module02 import *
fun01()
MyClass().fun02()
MyClass.fun03()

"""
    练习2:
    将信息管理系统分为四个模块.
    数据模型　-->  model.py
    XXXView --> usl.py
    　　　　　　　user  show  layer　用户表示层
　　XXXController --> bll.py
                     business  logic  layer 业务逻辑层
　　将调用View的代码 --> main.py
                      主要的/入口
"""











