"""
4. (扩展)对列表进行升序排序[3,8,6,5,2]
    思想:取元素(不要最后一个)
        作比较(与后面元素进行比较)
        如果发现后面元素更小，则与取出的元素进行交换.
    价值:列表中所有元素俩俩比较
"""
list01 = [3, 8, 6, 5, 2]

# 取元素： 第一个
# 作比较： 从第二个 ... 最后一个
# for c in range(1,len(list01)):
#     list01[0]   list01[c]
# 取元素： 第二个
# 作比较： 从第三个 ... 最后一个
# for c in range(2,len(list01)):
#     list01[1]   list01[c]
# 取元素： 第三个
# 作比较： 从第四个 ... 最后一个
# for c in range(3,len(list01)):
#     list01[2]   list01[c]

# 结论：
# 取元素
# for r in range(len(list01)-1):
#     作比较
#     for c in range(r+1, len(list01)):
#         list01[r] list01[c]

for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
# 10:10 上课
