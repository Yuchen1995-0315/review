# 练习：在终端获取年份(year),判断是否是闰年(True 是，Flase 不是)
# 条件：年份能被4整数，但是不能被100整除
#      年份能被400整除

year = int(input("请输入年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print("是否为闰年："+str(result))
