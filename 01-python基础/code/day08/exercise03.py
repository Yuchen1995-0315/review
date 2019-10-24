# 练习：调用print函数。
# print(*args, sep=' ', end='\n', file=None)

print()  # 换行

name = "qtx"
age = 18
# 得益于星号元组形参,所以才可以拼接多个不同类型变量.
print("我是:", name, "年龄是:", age)  # 换行
# 备注：命名关键字形参，使得以下代码可读性更高.
print(1, 2, 3, sep="--")  # 1--2--3
print(1, 2, 3, sep="--", end=" ")  # 1--2--3
