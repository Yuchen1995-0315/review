"""
    练习2: 在终端中循环录入人的信息(名字、年龄、性别、体重...),
      如果名称是空字符串，则停止。
      -- 将所有人的信息打印出来(一个人一行)
      -- 打印最后一个人的信息(名字、年龄、性别、体重...).
    数据结构：
    [
        {"name":"张无忌","age":26,"sex":"男","weight":50},
        {"name":"赵敏","age":24,"sex":"女","weight":40},
    ]

    总结：存储多个数据，使用什么数据结构？
          根据需求，结合优缺点，综合考虑(两害相权取其轻)

        列表
            优点：获取数据更为灵活(索引/切片)
            缺点：遍历元素获取数据，速度慢.

        字典：
            优点：根据key获取值，速度快.
            缺点：获取数据不灵活(键)
                 因为散列更占内存
"""

list_person_info = []
while True:
    name = input("请输入人的名称：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    sex = input("请输入性别：")
    weight = float(input("请输入体重："))
    dict_info = {"name": name, "age": age, "sex": sex, "weight": weight}
    list_person_info.append(dict_info)

for dict_item in list_person_info:
    print("%s的年龄是%d,性别是%s,体重是%f" % (dict_item["name"], dict_item["age"], dict_item["sex"], dict_item["weight"]))

dict_person = list_person_info[-1]
print("%s的年龄是%d,性别是%s,体重是%f" % (dict_person["name"], dict_person["age"], dict_person["sex"], dict_person["weight"]))
