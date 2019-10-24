""""
    列表推导式嵌套
    练习:exercise01.py
"""

# 需求:
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "可乐", "牛奶", "咖啡"]

# 笛卡尔积   全排列
# list_result = []
# for r in list01:
#     for c in list02:
#         list_result.append((r,c))

list_result = [(r, c) for r in list01 for c in list02]
print(len(list_result), list_result)
