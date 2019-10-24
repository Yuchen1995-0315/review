"""
    元组tuple
    练习:exercise07.py
    练习:exercise08.py
"""
# 1. 创建
tuple01 = (1, 2, 3, 4)
tuple02 = ()
# list 预留空间 -->  tuple 按需分配
tuple03 = tuple(["a", "b", "c"])
list03 = list(tuple03)

# tuple04 = ("a")  # 类型是str
tuple04 = ("a",)  # 如果元组中只有一个元素，那么必须加上逗号.
print(type(tuple04))

tuple05 = 1, 2, 3

# 可以直接从序列给多个变量赋值
name01, name02 = ("张无忌", "孙悟空")

# 2. 查询(索引/切片/循环)
print(tuple03[-1])
print(tuple03[::-1])  # 元组切片的结果还是元祖
for item in tuple03:
    print(item)

for i in range(len(tuple03) - 1, -1, -1):
    print(tuple03[i])
