"""
    程序入口
"""
from usl import StudentManagerView

# 如果当前模块不是主模块，则不执行代码
if __name__ == "__main__":
    try:
        view = StudentManagerView()
        view.main()
    except:
        print("出错啦")