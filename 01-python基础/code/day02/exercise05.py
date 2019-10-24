"""
     古代的秤，一斤是十六量.
     在终端中获取两，然后计算是几斤零几量
     显示格式：几斤零几量
"""
liang_weight = int(input("请输入两："))
jin = liang_weight // 16
liang = liang_weight % 16
print(str(jin) + "斤零" + str(liang) + "量")


