"""
    练习3:定义函数,将二维列表打印在终端(行列).
          测试用例
          [
            [1,2,3],             1 2 3
            [5,3,6]              5 3 6
          ]
"""


def print_double_list(list_target, str_end_char):
    """
        打印二维列表
    :param list_target:需要打印的二维列表
    :param str_end_char: 元素结束时的字符
    """

    # 遍历二维列表，得到的是一维列表(行)
    for list_row in list_target:
        for item in list_row:
            print(item, end=str_end_char)
        print()
    print()


list01 = [
    [1, 2, 3],
    [5, 3, 6]
]
print_double_list(list01, "\t")
