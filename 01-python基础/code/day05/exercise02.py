"""
    练习2：在终端中循环录入你喜欢的人名：
          如果录入空字符串,则停止。
          将所有人倒序打印在终端中（一人一行）
          要求：如果名称重复提示"已经存在"，不再存储。
"""
list_name = []
while True:
    name = input("请输入您喜欢的人名：")
    if name == "":
        break
    if name in list_name:
        print("已经存在")
    else:
        list_name.append(name)
# 通过切片访问列表元素(浅拷贝列表)
# for item in list_name[::-1]:
#     print(item)
# 通过索引访问列表元素
for i in range(len(list_name) - 1, -1, -1):
    print(list_name[i])
