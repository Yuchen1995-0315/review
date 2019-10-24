"""
    模块与包的重要概念
    1. 使用模块与包.可以让程序结构更加清晰。
    2. 多个模块/包之间的导入
    3. 导包是否成功?
       取决于sys.path中的路径(多个)与from的路径是否可以正确找到文件.

    模块相关的概念
        __name__
"""

# 1. 模块中定义隐藏成员(以单下划线命名的成员)
#    备注：类中定义私有成员(以双下划线命名的成员)
from module03 import *

fun01()
# _fun02()

# from module03 import _fun02
# _fun02()

# 2. 模块属性
import module03
# 获取模块的文档字符串
print(module03.__doc__)
# 获取模块的绝对路径
# /home/tarena/1908/month01/code/day14/module03.py
print(module03.__file__)

# 获取模块名称
# 作用:if __name__ == "__main__":
#  1. 如果是主模块，才执行程序逻辑.
#  2. 如果当前模块被导入，不执行测试逻辑。

print(__name__)# __main__
#
