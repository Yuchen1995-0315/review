"""
    练习1:定义函数,将一维列表打印在终端(一行).
          测试用例 [1,3,4,5] --> 1  3  4  5
"""


def print_list(list_target, str_end_char):
    """
        打印一维列表
    :param list_target:需要打印的一维列表
    :param str_end_char:每个元素结束时使用的字符
    """
    for item in list_target:
        print(item, end=str_end_char)
    print()

list01 = [1, 3, 4, 5]
print_list(list01, " ")

list02 = [6, 6, 7, 7]
print_list(list02, ".")

