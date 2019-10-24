"""
    选择语句
    练习：exercise01.py
         demo02.py
         exercise03.py
         exercise04.py
         exercise05.py
         exercise06.py

    if 条件:
        满足条件执行的代码
    else:
        不满足条件执行的代码

"""

# tab 选中的代码向右移动
# shift+tab 选中的代码向左移动
sex = input("请输入性别：")
# 如果是男的
# if sex == "男":
#     print("您好,先生！")
# else:
#     # 否则
#     print("您好,女士！")

if sex == "男":
    print("您好,先生！")
    # 否则 如果
elif sex == "女":
    print("您好,女士！")
else:  # 否则
    print("性别未知")

# 调试:让程序在指定的行中断,然后逐语句执行。
# 步骤:
#  1. 加断点（在可能出错的代码）
#  2. 调试
#  3. 逐语句执行
# 重点：
#  1. 审查程序执行流程
#  2. 检查变量取值
