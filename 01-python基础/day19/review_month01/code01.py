"""
    第一门课：python基础
    数据基本运算
        1. pycharm快捷键（标志着对开发工具的熟练程度,提高开发效率）
            -- 百度搜索

        2. 对象池：每次创建对象时，都会在池中查找是否具有相同对象，
                  如果有则直接返回其地址，如果没有再创建.
                  提高内存的利用率(减少重复出现的对象)
           小整数对象池:-5 ~ 256 之间的数字永远存在内存中.

        3. python内存管理机制(自动化)：
            引用计数:
                a = 对象()
                b = a
                del b,a  # 对象被销毁

                list01 = []
                list02 = []
                list01.append(list02)
                list02.append(list01)
                缺点：不能解决循环引用问题,容易造成内存浪费.
            标记清除：扫描内存，查看是否存在无法访问的内存空间。
                缺点：扫描内存耗时长.
            分代回收：将内存划分为多个区域("年轻代"、"中年代"、"老年代")
                    当上一代满了，进行标记清除，将有用的数据移动到下一代(升代)。
            内存优化：
                尽量少产生垃圾、对象池、手动回收(慎重)、
                （字符串拼接)
        4.容器
            每种容器特点：存储？ 可变？ 不可变？
            内存图
            各种容器互相转换
            注意：往往是根据数据，灵活的选择各种容器嵌套.
        5.函数
            设计：小而精，不要大而全.
            参数：
                实参
                    位置：函数名(1,2,3)
                        序列实参：函数名(*列表)
                    关键字：函数名(a = 1,c = 3, b=2)
                        字典实参：函数名(**字典)
                形参
                    默认形参：def 函数名(a =0,b=0.0,c="")  --可以不传递
                    位置：def 函数名(a,b,c)   -- 必须传递
                        星号元组形参：def 函数名(*args)-- 位置实参数量无限
                    命名关键字形参： def 函数名(*args,a) -- a 必须使用关键字实参
                                  def 函数名(a,*,b) -- b 必须使用关键字实参
                        双星号字典形参：def 函数名(**kwargs)-- 关键字实参数量无限
"""

a = 500
b = 500
print(a is b)  # true

a = "悟空"
b = "悟空"
print(a is b)  # true

a = (1, 2)
b = (1, 2)
print(a is b)  # false

def fun01(*args,a):
    pass

fun01(12,3,123,4,4,53,456,a = 1)
