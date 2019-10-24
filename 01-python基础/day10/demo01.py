"""
    封装
        封装数据:多个数据 合成 一个数据
            优势：
                 将数据与对数据的操作相关联（合为一体）。
                 代码可读性更高（类是对象的模板）。
            例如：老婆(数据：身高、体重、姓名.行为：工作)
                 狗(数据：爱称、品种、年龄.行为：玩、坐下)
        封装行为：对外提供[必要]的功能,隐藏实现细节(方法体/方法本身).
"""


class Wife:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    # 方法隐藏实现的细节(方法体)
    def print_weight(self):
        if self.weight > 50:
            print("你猜")
        else:
            print("体重是：", self.weight)

    # 隐藏方法：使用双下滑下命名
    def __fun01(self):
        print("不想说的事")


w01 = Wife("芳芳", 40)
w01.print_weight()

# 不能调用私有成员
# w01.__fun01()
