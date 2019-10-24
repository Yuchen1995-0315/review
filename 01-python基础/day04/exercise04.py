# 练习：累加10--50之间，个位不是2、5、9的整数
sum_value = 0
for item in range(10, 51):
    unit01 = item % 10
    if unit01 == 2 or unit01 == 5 or unit01 == 9:
        continue
    sum_value += item
print(sum_value)

# 总结：
# 循环语句
# for：预定次数  for item in range(次数)
#     经典案例：3道考试题
# while：不知道次数，但知道循环条件。while 条件：
#     经典案例：纸张对折到8848m。
# 循环的价值：累加4位整数  -变成-> 累加n位整数