"""
     练习2：在终端中获取一个商品单价。5
           再获取一个购买的数量.3
           最后获取支付的金额。20
           计算应该找回多少钱。5    20 - 5 × 3
"""
# 备注：float()  int()  存在输入错误的风险
# 15:25 上课
str_price = input("请输入一个商品单价：")
float_price = float(str_price)

str_count = input("请输入一个购买的数量：")
int_count = int(str_count)

money = float(input("请输入支付的金额："))

result = money - float_price * int_count

print("结果是："+str(result))
