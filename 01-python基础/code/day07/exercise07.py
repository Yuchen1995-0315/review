# 练习: 将以下功能, 封装到函数中。
# 定义排序函数
"""
list01 = [3, 8, 6, 5, 2]

for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
"""

def sort(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    # return list_target  # 1. 传入的是可变对象 2. 函数体改变的是可变对象

list01 = [3, 8, 6, 5, 2]
# print(sort(list01))
sort(list01)
print(list01)

# 17:05









