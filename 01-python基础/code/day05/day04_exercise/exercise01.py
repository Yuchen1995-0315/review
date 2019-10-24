"""
3. 在终端中获取一个整数，
    作为边长，打印矩形。
    例如:边长3
    ***
    * *
    ***
    例如:边长5
    *****
    *   *
    *   *
    *   *
    *****
"""

number = int(input("请输入整数："))
print("*" * number)
for item in range(number - 2):
    print("*" + " " * (number - 2) + "*")
print("*" * number)
