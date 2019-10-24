"""
    在不改变旧功能(fun01，fun02)基础上，为其增加新功能(打印方法执行时间)
    公式：执行时间 = 开始后 - 开始前
"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # 旧功能
        result = func(*args, **kwargs)
        stop_time = time.time()
        # 新功能
        print(stop_time - start_time)
        return result

    return wrapper

@print_execute_time
def fun01():
    for i in range(10):
        pass

@print_execute_time# fun02 = print_execute_time(fun02)
def fun02():
    for i in range(1000000):
        pass


fun01()
fun02()
