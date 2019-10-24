"""
    装饰器
    练习：exercise06
"""

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper

# 增加新功能：打印函数名称
# def print_func_name(func):
#     print(func.__name__)

# print_func_name(print)

@print_func_name
def say_hello():
    print("hello")


@print_func_name
def say_goodbye():
    print("goodbye")


say_hello()
say_goodbye()
