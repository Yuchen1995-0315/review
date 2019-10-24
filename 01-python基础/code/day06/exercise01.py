"""
    练习1: 在终端中循环录入商品信息(名称、价格),
          如果名称是空字符串，则停止。
          -- 将所有商品的名称与价格打印出来(一个商品一行)
          -- 如果录入了"游戏机",则单独打印其价格.
"""
dict_commodity_info = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = float(input("请输入价格："))
    dict_commodity_info[name] = price
for k, v in dict_commodity_info.items():
    print("%s商品的价格是%f" % (k, v))
if "游戏机" in dict_commodity_info:
    print(dict_commodity_info["游戏机"])










