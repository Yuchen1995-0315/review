"""
    练习1: 将day04/exercise01功能,封装到函数中。

    # 在终端中获取一个四位整数，计算每位相加和.
    str_number = input("请输入整数：")
    result = 0
    for item in str_number:
        result += int(item)
    print(result)
"""


def each_unit_sum(str_number):
    """
        遍历字符串类型整数的每位，然后求和.
    :param str_number:需要计算的str类型的整数
    :return: 求和的结果
    """
    result = 0
    for item in str_number:
        result += int(item)
    return result

re = each_unit_sum("12345")
print(re)
print(each_unit_sum("65788908908965756"))



