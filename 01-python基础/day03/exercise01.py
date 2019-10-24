# 练习：在day02/exercise04.py基础上，增加新功能。
# 如果钱不够提示"金额不足"
# 否则提示"应找回：xx元"

str_price = input("请输入一个商品单价：")
float_price = float(str_price)
str_count = input("请输入一个购买的数量：")
int_count = int(str_count)
money = float(input("请输入支付的金额："))
result = money - float_price * int_count

if result < 0:
    print("金额不足")
else:
    print("应找回："+str(result)+"元")


