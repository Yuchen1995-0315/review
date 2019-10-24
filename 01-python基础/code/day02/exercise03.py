"""
    练习1：在终端中获取一个变量
          再获取另外一个变量
          然后编写程序，交换两个变量的数据.
          最后打印两个变量
"""
variable01 = input("请输入第一个变量：")
variable02 = input("请输入第二个变量：")
# temp = variable01
# variable01 = variable02
# variable02 = temp
variable01,variable02 = variable02,variable01
print("变量1是：" + variable01)
print("变量2是：" + variable02)


