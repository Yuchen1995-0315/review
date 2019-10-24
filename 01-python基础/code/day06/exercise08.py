# 练习:矩阵转置
# 将list01中的每列，存储到list02中的每行(列表)。
list01 = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 8, 10, 11],
]

list02 = []


#list01[0][0]
#list01[1][0]
#list01[2][0]

for c in range(4):
    line = []
    for r in range(3):
        line.append(list01[r][c])
    list02.append(line)

print(list02)
