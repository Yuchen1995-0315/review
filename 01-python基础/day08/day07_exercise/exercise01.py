"""
    (扩展)方阵(行数列数相同)转置
"""

list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
"""
# list01[1][0] list01[0][1]
# list01[2][0] list01[0][2]
# list01[3][0] list01[0][3]
for r in range(1, 4):
    # list01[r][0]  <-->  list01[0][r]
    pass
# list01[2][1] list01[1][2]
# list01[3][1] list01[1][3]
for r in range(2, 4):
    # list01[r][1]  <-->  list01[1][r]
    pass
# list01[3][2] list01[2][3]
for r in range(3, 4):
    # list01[r][2]  <-->  list01[2][r]
    pass

for c in range(1, 4):  # 1 2 3
    for r in range(c, 4):
        # list01[r][c-1]  <-->  list01[c-1][r]
        pass
"""


def square_matrix_transposition(list_matrix):
    """
        方阵转置（列转换为行）
    :param list_matrix: 需要转置的方阵
    :return:
    """
    for c in range(1, len(list_matrix)):  # 1 2 3
        for r in range(c, len(list_matrix)):
            list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]

# 方阵转置的转置，等于原方阵
square_matrix_transposition(list01)
print(list01)

square_matrix_transposition(list01)
print(list01)