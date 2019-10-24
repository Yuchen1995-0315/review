"""
    list 内存图
    练习:exercise01.py
        exercise02.py
        exercise03.py
"""
list01 = ["唐僧", "悟空", "八戒"]
list01.append("沙僧")
# 将list01存储的列表地址赋值给list02(两个变量指向同一个列表对象)
list02 = list01
list01[0] = "唐三藏"
print(list02[0])  # "唐三藏"

list01 = [800, 1000]
list01.append(900)
# 将list01指向的列表拷贝一份(创建了新列表),再赋值给list02(两个变量指向不同的列表对象)
list02 = list01[:]
# 所以修改其中一个列表对象，不影响另外一个列表对象.
list01[0] = 500
print(list02[0])  # 800

list01 = [300]
list02 = list01
# 修改的是变量list01的指向（列表对象没有变化）
list01 = 500
print(list02[0])  # 300

list01 = [300, 400, 500]
# 将list01指向的列表倒叙拷贝一份(创建新列表)
list02 = list01[::-1]
# 遍历列表["四百","五百","六百"],将所有元素插入到list01指向的列表中。
list01[1:2] = ["四百", "五百", "六百"]
print(list01)
print(list02)

list01 = [1, 2]
# 向列表追加一个元素(列表)
list01.append([3, 4])
# list02 = list01[:]
# 浅拷贝
list02 = list01.copy()
# 修改列表第三个元素（列表）的第一个元素
list01[2][0] = "三"
print(list02[2][0])

list01 = [100, [200, 300]]
# 将list01存储的列表地址赋值给变量list02
list02 = list01
# 将list01存储的列表浅拷贝一份(创建新列表)
list03 = list01[:]
# 同上
# list03 = list01.copy()
# 深拷贝
import copy

list04 = copy.deepcopy(list01)
# 优点：深拷贝后的数据，与之前的数据互不影响。
# 缺点：由于拷贝整个依赖的数据，所以特别占用内存。


list01 = [500, 600, 700]
list02 = [500, 600, 700]
# 比较的是list01指向的对象与list02指向的对象
print(list01 == list02)# true
# is 比较的是变量list01存储的地址与变量list02存储的地址
print(list01 is list02)# false
# is 的本质比较地址 id(变量)  返回变量指向的对象地址
print(id(list01) == id(list02)) # false

