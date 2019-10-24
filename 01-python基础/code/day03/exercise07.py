# 练习1：在终端中录入一个整数，如果是奇数为变量state赋值"是奇数",
#        否则赋值"是偶数"。

# number = int(input("请输入整数："))
# if number % 2 == 1:
#     state = "是奇数"
# else:
#     state = "是偶数"

# number = int(input("请输入整数："))
# if number % 2:
#     state = "是奇数"
# else:
#     state = "是偶数"

state = "是奇数" if int(input("请输入整数：")) % 2 else "是偶数"
print(state)
# 练习2：在终端中录入一个年份，如果是闰年为变量day赋值29,
#        否则赋值28。
# year = int(input("请输入年份："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     day = 29
# else:
#     day = 28
# 不建议，太绕了。
# year = int(input("请输入年份："))
# if not year % 4 and year % 100 or not year % 400:
#     day = 29
# else:
#     day = 28
year = int(input("请输入年份："))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
