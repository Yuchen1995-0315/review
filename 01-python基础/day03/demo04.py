"""
    while 循环

    while 条件:
        循环体

    练习:exercise08
"""

# 死循环：循环条件永远满足
while True:
    str_usd = input("请输入美元：")
    int_usd = float(str_usd)
    result = int_usd * 7.1393
    print("结果是：" + str(result))

    if input("输入e键退出") == "e":
        break  # 退出循环体




