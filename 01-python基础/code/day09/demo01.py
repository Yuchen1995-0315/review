"""
    面向对象
        字面意思：考虑问题从对象的角度出发
                找？干？
        类与对象：
            对象：真实存在　　　　（万物皆对象）
            类：抽象概念　　　类别　　　模板
            老婆类
                数据（变量）：名词性的修饰信息
                    名字、身高、体重、．．．
                行为（函数／方法）：动词性的行为
                    挣钱、做饭、打人

            变量　= 老婆类()
"""

# 11:35　上课
class Wife:
    """
        抽象的老婆类
    """
    # 数据成员
    def __init__(self, name, height=180, weight=50):
        self.name = name
        self.height = height
        self.weight = weight

    def work(self):
        # 方法如果正确找到自己的数据？
        # 通过self
        print(self.name + "工作了")

# 创建客观存在的老婆对象
w01 = Wife("丽丽", 170)  # 调用__init__方法
w01.work()  # 调用work方法,自动传递对象地址
