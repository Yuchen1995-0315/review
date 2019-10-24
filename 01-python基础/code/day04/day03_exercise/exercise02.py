"""
    在终端中获取年龄，显示
    婴儿(0-1)、儿童(2-13)、青少年(14-20)、成年人(21-65)、老年人(66--150)、仙人(上不封顶)
"""

age = int(input("请输入年龄："))
if age < 0:
    print("输入有误")
elif age <= 1:
    print("婴儿")
elif age <= 13:
    print("儿童")
elif age <= 20:
    print("青少年")
elif age <= 65:
    print("成年人")
elif age <= 150:
    print("老年人")
else:
    print("仙人")
