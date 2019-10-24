"""
    练习:定义函数，在控制台中获取年龄.
        要求:如果异常，或者年龄超过范围(0 -- 150)则重复获取
             直到正确为止.
"""


def get_age():
    while True:  # 重复
        try:
            age = int(input("请输入年龄："))# 如果异常执行17行代码
            if 0 <= age <= 150:
                return age
            else:
                print("年龄超过范围")
        except:  # 异常状态 --> 正常状态
            print("输入有误")

print(get_age())

# 练习:对信息管理系统进行异常处理,要求：按照程序既定流程执行。