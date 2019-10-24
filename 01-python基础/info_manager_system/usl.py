"""
   user  show  layer　用户表示层
"""
from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("""
1) 添加学生信息
2) 显示学生信息
3) 删除学生信息
4) 修改学生信息
5) 按照成绩从高到低显示 
        """)

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__outout_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        while True:
            name = input("请输入姓名:")
            # age = int(input("请输入年龄："))
            age = self.__input_number("年龄")
            score = self.__input_number("成绩")
            stu = StudentModel(name, age, score)
            # StudentManagerController().add_student(....)
            self.__manager.add_student(stu)
            if input("输入e退出:") == "e":
                break

    def __input_number(self, message):
        while True:
            try:
                number = int(input("请输入%s:"%message))
                break
            except:
                print("输入有误.")
        return number

    def __output_students(self):
        for item in self.__manager.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        # id = int(input("请输入需要删除的编号："))
        id = self.__input_number("需要删除的编号")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        # stu.id = int(input("请输入需要修改的学生编号："))
        stu.id = self.__input_number("需要修改的学生编号")
        stu.name = input("请输入需要修改的学生姓名：")
        # stu.age = int(input("请输入需要修改的学生年龄："))
        stu.age = self.__input_number("需要修改的学生年龄")
        # stu.score = int(input("请输入需要修改的学生成绩："))
        stu.score = self.__input_number("需要修改的学生成绩")

        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __outout_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students()