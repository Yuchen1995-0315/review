"""
    列表
        与字符串最大的区别：存储字符与存储变量、可变与不可变
    练习：exercise08.py
"""

# 1. 创建
list01 = ["悟空",50,1.5,True]
list02 = list("齐天大圣")# "齐天大圣" --> ["齐","天","大","圣"]
print(list02)
# 空列表
list03 = []
list04 = list()

# 2. 查询(索引/切片/循环)
print(list01[-1])
# 通过切片访问元素，会创建新列表
print(list01[1:3])
for item in list01:
    print(item)

# 3. 增加
# 追加
list01.append("唐僧")
# 插入
list01.insert(1,"八戒")

print(list01)
# 4.修改
list01[0] = "孙悟空"
# 通过切片修改元素，不会创建新列表
# list01[2:5] = [1,2,3]
# list01[2:5] = [1]
# list01[2:5] = [1,23,4,234,245,43,5,53,6]
# list01[2:5] = 100 # 不是可迭代对象，不能通过切片修改.
print(list01)

# 5.删除  del 变量
# del
del list01[0]
del list01[1:3]
# 根据元素
list01.remove("唐僧")
print(list01)





