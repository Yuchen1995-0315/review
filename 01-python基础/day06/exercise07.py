list01 = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 8, 10, 11],
]

# 练习1：打印二维列表第二行(一个数据一行)
# list01[1][0]   list01[1][1]  list01[1][2]  list01[1][3]
for c in range(len(list01[1])):  # 0 1 2 3
    print(list01[1][c])

# 练习2：打印二维列表第三列(一个数据一行)
# list01[0][2]
# list01[1][2]
# list01[2][2]
for r in range(len(list01)):  # 0 1 2
    print(list01[r][2])


# 练习3：打印二维列表(行列)
# # list01[0][0]   list01[0][1]   list01[0][2]   list01[0][3]
# for c in range(4):#0123
#     print(list01[0][c],end = " ")

# # list01[1][0]   list01[1][1]   list01[1][2]   list01[1][3]
# for c in range(4):#0123
#     print(list01[1][c],end = " ")
for r in range(len(list01)):  # 0 1 2
    for c in range(len(list01[r])):  # 0123
        print(list01[r][c], end="\t")
    print()
