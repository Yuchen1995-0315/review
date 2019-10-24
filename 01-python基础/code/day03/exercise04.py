"""
    练习:在终端中录入4个同学的体重
        打印最重的数字。
    思路：假设第一个就是最大值
         如果第二个大于假设的，那么替换假设的。
         如果第三个大于假设的，那么替换假设的。
         如果第四个大于假设的，那么替换假设的。
         最终，假设的就是最大的。
"""
number01 = float(input("请输入第1个体重："))
number02 = float(input("请输入第2个体重："))
number03 = float(input("请输入第3个体重："))
number04 = float(input("请输入第4个体重："))

max_value = number01
if number02 > max_value:
    max_value = number02
if number03 > max_value:
    max_value = number03
if number04 > max_value:
    max_value = number04

print(max_value)
