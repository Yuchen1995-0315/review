"""
    集合
    价值：去重复(容器转换)
"""

# 1. 创建
set01 = {"悟空", "八戒", "唐僧"}
print(type(set01))
# set02 = {} # 创建的是字典，不是集合.
set02 = set([23, 78, 5, 78, 67, 78, 78])
set03 = set({"a": "A", "b": "B"})

# 2. 查询(循环)
for item in set01:
    print(item)

# 3. 添加
set01.add("白龙马")

# 3. 修改(由于无法定位元素，所以改不了)
# 4. 删除
# set01.remove("悟空2")# 如果不存在则错误
set01.discard("悟空2")# 即使不存在也不会错误
print(set01)

# 数学运算
set01 = {1, 2, 3}
set02 = {2, 3, 4}
# 交集 (重合)
print(set01 & set02)  # {2, 3}
# 并集
print(set01 | set02)  # {1, 2, 3, 4}
# 对称补集
print(set01 ^ set02)  # {1, 4}
print(set01 - set02)  # {1}
print(set02 - set01)  # {4}
# 子集(set03) 超集(set01)
set03 = {2, 3}
print(set03 < set01)  # true


