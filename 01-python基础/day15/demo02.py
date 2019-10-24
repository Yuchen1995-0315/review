"""
    异常处理
    练习：exercise03
    练习:信息管理系统
    练习:购物车 shopping__oo.py
"""


def div_apple(apple_count):
    """
        分苹果
    """
    person_count = int(input("请输入人数："))  # ValueError
    result = apple_count / person_count  # ZeroDivisionError
    print("每人%d个苹果" % result)

# 处理目的：让异常(错误)流程 转换为 正常流程

""" 1. 统一处理所有异常
try:
    # 可能出错的代码
    div_apple(10)
# except Exception:# 可以拦截所有错误(异常)
except:
    print("程序出错啦")

print("后续逻辑")
"""

""" 2. 分门别类的处理各种异常（官方更建议）
try:
    # 可能出错的代码
    div_apple(10)
except ValueError:
    print("输入的不是整数，所以错误啦.")
except ZeroDivisionError:
    print("输入的是零，所以错误啦.")

print("后续逻辑")
"""

""" 可以处理错误执行逻辑，也可以处理没出错的执行逻辑
try:
    # 可能出错的代码
    div_apple(10)
except ValueError:
    print("输入的不是整数，所以错误啦.")
except ZeroDivisionError:
    print("输入的是零，所以错误啦.")
else:
    print("没出错执行的逻辑")

print("后续逻辑")
"""

try:
    # 可能出错的代码
    div_apple(10)
finally:
    # 如果出错了，虽然我解决不了，但有个事我必须做.
    print("管你错不错呢，一定做！")

print("后续逻辑")











