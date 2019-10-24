"""
    一个小球从100米高度落下
    每次弹回原高度一半
    请计算：
        (1)总共弹起来多少次(最小弹起高度是0.01m)?
        (2)整个过程总共走了多少米?
"""
height = 100
count = 0
distance = height
# 当前高度
# while height > 0.01:
# 弹起来的高度
while height / 2 > 0.01:
    count += 1
    # 弹起来
    height /= 2
    # print("第%d次弹起高度是%f米." % (count, height))
    distance += height * 2  # 累加起/落距离

print("总共弹起来%d次。" % count)
print("总共经过%.2f米" % distance)
#  10:15 上课
