"""
    包中的特殊模块__init__.py
        1. 标志着这个文件夹是包
        2. 当导入当前包时自动执行
"""

print("我是__init__.py")
__all__ = ["p01","p02"]