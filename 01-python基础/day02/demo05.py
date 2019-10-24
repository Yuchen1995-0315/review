"""
    数据类型
        复数
        bool
    运算符
        比较
        逻辑
    练习：exercise08.py
"""
# 1.复数 = 实部 + 虚部
a = 10 + 3j
print(type(a))

# 2. bool 命题：带有判断性质的陈述句。
# 例如：我是一个男人.  结果：对True    错Flase
num01 = 10
num02 = 3
b = 10 < 3
print(b)  # F

# 3. 比较运算符 >   <  >=   <=  相同 ==   不同!=
print(10.5 > 5)  # 如果不能参与比较运算，会报错。

# 4. 逻辑运算符   and  or   not
# 判断bool的关系
# and 表示并且的关系（都得满足）, 现象：一假俱假
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# or 表示或者的关系（满足一个就行）, 现象：一真俱真
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
# 非 （取反）
b = True
c = not b
print(c)  # False
