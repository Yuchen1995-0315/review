"""
    使用可迭代对象
"""

list01 = [234, 45, 54, 65, 6, 7, 8]

# 可以被for的条件：
#    对象具有__iter__方法

# for itme in list01:
#     print(itme)

# for原理:
# 1.  获取迭代器对象
iterator = list01.__iter__()
# 2. 获取下一个元素（迭代一次）
while True:
    try:
        item = iterator.__next__()
        print(item)
    # 3. 拦截StopIteration异常
    except StopIteration:
        break
