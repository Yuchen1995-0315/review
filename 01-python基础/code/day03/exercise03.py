# 练习:在终端中录入一个数字：
#     再终录入一个运算符：
#     最后终录入另外一个数字：
#     根据运算符计算数字
#     要求：运算符+-*/,如果输入其他符号，提示：运算符输入有误。

number_one = float(input("请输入第一个数字："))
operator = input("请输入运算符：")
number_two = float(input("请输入第二个数字："))
if operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "/":
    print(number_one / number_two)
else:
    print("运算符输入有误")
