"""
    ｐｙｔｈｏｎ程序结构

    项目(文件夹)
        包
            模块
                全局变量
                函数
                类
                    方法
                        语句
                    数据
    练习:　my_project
"""
# 方式1
# import 从项目根目录开始的路径.模块 as 别名
# 别名.成员
# import package01.package02.p01 as p
# p.fun01()

# 方式2
# from 从项目根目录开始的路径.模块 import 成员
# 直接使用成员
from package01.package02.p01 import fun01
fun01()

# from 从项目根目录开始的路径 import 模块
# 模块.成员
# from package01.package02 import p01
# p01.fun01()

# 方式3
# from package01.package02.p01 import *
# fun01()

# 备注: 必须在package02的__init__.py模块中设置　__all__属性
# from package01.package02 import *
# p01.fun01()
# p02.fun02()










