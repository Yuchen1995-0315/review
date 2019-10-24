"""
    模块
        导入
    练习1:exercise01
    15:30
"""

# 备注：如果希望不出现错误提示(有智能提示)
#      需要将模块所在文件夹标记为"项目根目录"-- Mark Directory -- Sources Root
# 方式1:import 模块
#      模块.成员
# 本质：创建一个变量(模块名称),关联导入的模块。
# import module01

# module01.fun01()

# import module01 as m # 给模块起一个别名
#
# m.fun01()

# 方式2： from 模块名 import 成员
#         直接使用成员
# 本质：将模块成员导入到当前作用域中

from module01 import fun01

fun01()

# 方式3：from 模块名 import *
#       直接使用该模块所有成员
# 缺点：如果对应该模块成员不熟悉，容易造成命名冲突(覆盖).
from module01 import *

fun02()


def fun03():
    print("demo01 -- fun03")


fun03()
