"""
    数据类型转换
        int  float   str

    运算符

    练习:exercise03.py
        exercise04.py
        exercise05.py
        exercise06.py
        exercise07.py

"""
# 1. 类型转换
str01 = "100"
# str -->  int
# 注意：如果字符串存储的数据,不像整形,转换失败.
int01 = int(str01)
re = int01 + 1
# int --> str
print("结果是：" + str(re))

# 2. 运算符
# (1)算数运算符+ - * /  //  %  **
num01 = 5
num02 = 2
print(num01 / num02)  # 2.5   除法：取最终结果
print(num01 // num02)  # 2    除法：取整数商
print(num01 % num02)  # 6    除法：取余数
print(56 % 10)  # 获取个位

print(2 ** 6)
# (2) 增强运算符+=  -=  *=  /=   //=   %=  **=
num03 = num01 + 5  # 不会改变num01
num01 = num01 + 5  # 变量num01 加5后创建新对象，又赋值给自身.
print(num01)  # 10

num01 += 5 # 相当于 num01 = num01 + 5
