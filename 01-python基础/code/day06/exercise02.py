"""
    练习2: 在终端中循环录入人的信息(名字、年龄、性别、体重...),
          如果名称是空字符串，则停止。
          -- 将所有人的信息打印出来(一个人一行)
          -- 如果录入了"张无忌",则单独打印其信息(名字、年龄、性别、体重...).
    数据结构：
    {
        "张无忌":[26,"男",50],
        "赵敏":[24,"女",40]
    }
"""

dict_person_info = {}
while True:
    name = input("请输入人的名称：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    sex = input("请输入性别：")
    weight = float(input("请输入体重："))
    dict_person_info[name] = [age, sex, weight]

for k_name, v_info in dict_person_info.items():
    print("%s的年龄是%d,性别是%s,体重是%f" % (k_name, v_info[0], v_info[1], v_info[2]))

if "张无忌" in dict_person_info:
    list_info = dict_person_info["张无忌"]
    print("张无忌的年龄是%d,性别是%s,体重是%f" % (list_info[0], list_info[1], list_info[2]))
