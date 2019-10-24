"""

"""


class Wife:

    def __init__(self, name, height=180, weight=50):
        self.name = name
        self.height = height
        self.weight = weight

    def print_self(self):
        print(self.name,self.height,self.weight)


list_wife = [
    Wife("丽丽", 150, 40),
    Wife("芳芳", 170, 50),
    Wife("锤锤", 178, 90),
    Wife("二狗", 120, 56),
]
# 1. 在终端中打印所有老婆(一行一个)
for item in list_wife:
    item.print_self()

# 2. 找出姓名是"锤锤"的老婆对象，然后打印其所有数据。
for item in list_wife:
    if item.name == "锤锤":
        item.print_self()

# 3. 将身高大于150的老婆，体重增加5.
#    测试：将所有老婆信息打印出来
for item in list_wife:
    if item.height > 150:
        item.weight += 5

print(list_wife)

# 4. 将所有老婆的名字，单独存储到列表中。
#     测试：打印列表
list_name = []
for item in list_wife:
    list_name.append(item.name)

print(list_name)










