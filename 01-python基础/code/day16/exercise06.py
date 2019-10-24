"""
    练习1:从列表[4,54,5,6,7,8,9]中获取所有偶数
         -- 传统思想：定义函数，将结果存入列表，再返回列表
         -- 生成器思想：定义生成器函数实现，使用yield返回结果.
         通过调试，体会两种思想的差异，与生成器的魅力.
"""
list01 = [4, 54, 5, 6, 7, 8, 9]


def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result


re = get_even01()
for item in re:
    print(item)


def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item

# 返回多个数据
re = get_even02()
# 循环一次 计算一次 返回一次
for item in re:
    print(item)


