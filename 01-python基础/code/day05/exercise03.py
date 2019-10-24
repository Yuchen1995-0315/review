# 练习3：将列表[4,5,6,4,8,9]中所有偶数删除

list01 = [4, 5, 6, 4, 8, 9]
# for item in list01:
#     if item % 2 == 0:
#         # 删除的是变量item，而不是列表中的元素
#         del item

# for i in range(len(list01)):
#     if list01[i] % 2 == 0:
#         # 删除列表中的元素
#          删除元素时，后一个元素向前赋值，总会错过。
#         del list01[i]
#

# 方案1
# for i in range(len(list01)-1,-1,-1):
#     if list01[i] % 2 == 0:
#         del list01[i]
#

# 方案2
# for item in list01[::-1]:
#     if item % 2 == 0:
#         list01.remove(item)
# 15:30 上课
for i in range(len(list01)-1,-1,-1):
    if list01[i] % 2 == 0:
         list01.remove(list01[i])

print(list01)
