"""
    复习
    容器
        str: 存储字符编码，不可变,序列.
        list:存储变量，可变,序列.
        tuple:存储变量，不可变,序列.

        dict:存储键值对，可变,散列.
              键：不可变，唯一
        set:存储键，可变,散列.
        frozenset:不可变的set

        可变：预留空间
        不可变：按需分配
        容器间转换：略..
        容器嵌套:list   dict

    for for

"""

# 固定集合
list01 = [1,1,2,3]
# set01 = set(list01)# 缺点：预留空间
frozenset01 = frozenset(list01)
list01 = list(frozenset01)
print(list01)
