"""
将元组(4,5,15,6,7,8)中最大的数字找出来。(不使用max)
    思想:假设第一个元素就是最大的
         依次与后面的元素进行比较，如果大于假设的，则替换。
"""
tuple01 = (4, 5, 15, 6, 7, 8)
max_value = tuple01[0]
# 与后面元素（  tuple01[i] ）进行比较
for i in range(1, len(tuple01)):
    if max_value < tuple01[i]:
        max_value = tuple01[i]
print(max_value)
