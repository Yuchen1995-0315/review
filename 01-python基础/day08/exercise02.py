# 练习:定义函数,多个数值相加的函数.
def sum(*args):
    result = 0
    for item in args:
        result += item
    return result


print(sum(1,2))
print(sum(1,2,3,54,3,5,65,67))

