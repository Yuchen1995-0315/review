"""
    练习:
        定义员工管理器
            1. 记录所有员工
            2. 提供计算总工资的方法

        员工种类：
            程序员：底薪 + 项目分红
            测试员:底薪 + bug数 × 5元
            ....

        要求：增加新员工种类，不影响员工管理器
        体会：继承与组合
"""

# 11:35
class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def calculate_total_salary(self):
        total_salary = 0
        for item in self.__employees:
            total_salary += item.get_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary


# --------------------------------------

class Programmer(Employee):
    def __init__(self, base_salary=0, bonus=0):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus


class Tester(Employee):
    def __init__(self, bug_count, base_salary):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_salary(self):
        return self.base_salary + self.bug_count * 5


# 测试
manager = EmployeeManager()
manager.add_employee(Programmer(10000, 100000))
manager.add_employee(Tester(8000, 100))

print(manager.calculate_total_salary())
