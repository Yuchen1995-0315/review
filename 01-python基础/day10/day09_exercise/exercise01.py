"""
4. 创建学生类(数据:姓名,性别,年龄,成绩.行为:打印个人信息.)
   创建学生列表
   -- 查找姓名是"张无忌"的学生对象(调用打印个人信息方法)
   -- 查找所有学生的姓名与成绩,形成一个列表
   -- 查找所有年龄在25以上并且成绩及格的学生(调用打印个人信息方法)
   -- 将所有学生成绩增加10分
   -- 删除不及格的学生
   要求：画出内存图.
"""


# 10:05
class Student:
    """
        学生类
    """

    def __init__(self, name, sex="", age=0, score=0.0):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def print_self(self):
        print(self.name, self.sex, self.age, self.score)


list_student = [
    Student("诸葛亮", "男", 65, 101.5),
    Student("张飞", "男"),
    Student("赵云", "男", 26),
    Student("小乔", "女", 18, 95),
    Student("张无忌", "男", 26, 90),
]

# 1.
for item in list_student:
    if item.name == "张无忌":
        item.print_self()

# 2.
# list_info = []
# for item in list_student:
#     list_info.append((item.name,item.score))

list_info = [(item.name, item.score) for item in list_student]
print(list_info)

# 3. 找所有年龄在25以上并且成绩及格的学生(调用打印个人信息方法)
for item in list_student:
    if item.age > 25 and item.score >= 60:
        item.print_self()

# 4.
for item in list_student:
    item.score += 10

# 5.
for i in range(len(list_student) - 1, -1, -1):
    if list_student[i].score < 60:
        del list_student[i]

print()
