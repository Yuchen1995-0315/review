"""
    day06 复习
    容器
        str：存储字符编码值，不可变序列.
        list：存储变量，可变序列.         【预留空间】
        tuple：存储变量，不可变序列.      【按需加载】
        ...
        创建
            str01 = ""
            str02 = str(其他类型对象)

            list01 = []
            list02 = list(可迭代对象)

            tuple01 = ()
            tuple02 = tuple(可迭代对象)

        查询(索引/切片/循环)
            print(str01[-1])
            print(list01[-3:])
            for itme in tuple02:
                print(itme)
            for i in range(len(tuple02)-1,-1,-1):
                print(tuple02[i])

        修改
            str01 += "a"
            tuple01 += ("a",) # 容器拼接后产生新对象
            list01 += ["a"] # 在原有列表基础上增加新元素
            list01[0] = 数据
            list01[1:3] = 可迭代对象

        删除
            list01.remove(元素)
            del list01[索引]
            del list01[切片]

        通用操作
            +  *  ==  ！=   in
"""
tuple01 = ("e",)
# print(id(tuple01))
tuple01 += ("a",)
# print(id(tuple01))
print(tuple01)


list01 = ["e"]
print(id(list01))
# list01.append("a")
list01 += ["a"]
print(id(list01))

print(list01)
