"""
    字典
    练习：exercise01.py
         exercise02.py
         exercise03.py
"""
# 11:20上课

# 1. 创建
dict01 = {101:"悟空"}
dict02 = {}

dict03 = dict([("a","b"),("c","d")])
print(dict03)

#2. 查询(键/循环)
print(dict03["a"])

# 获取所有key
for key in dict03:
    print(key)
    print(dict03[key])

for element in dict03.items():
    print(element)# 元组

# 获取所有记录(键值对)
for k,v in dict03.items():
    print(k)
    print(v)

# 获取所有值
for v in dict03.values():
    print(v)

# 注意：如果查找不存在的key,会报错
if "q" in dict03:
    print(dict03["q"])

# 3.增加 dict03[键] = 值
dict03["bj"] = "八戒"
dict03["ds"] = "大圣"

# 4. 修改
dict03["ds"] = "齐天大圣"

# 5. 删除
del dict03["bj"]

print(dict03)






