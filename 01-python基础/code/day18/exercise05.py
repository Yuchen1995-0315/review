"""
    闭包应用
         逻辑连续
         装饰器
"""


# 压岁钱
def give_gife_money(money):
    def child_buy(target, price):
        nonlocal money
        if money >= price:
            money -= price
            print("孩子买了%s,花了%.1f钱" % (target, price))

        else:
            print("钱不够了，呜呜呜～")

    return child_buy



action = give_gife_money(10000)
action("变形金刚", 200)
action("天安门模型", 500)
action("手机", 12000)
