"""
    练习：
    1. 创建列表，存储八大行星.
    2. 打印距离太阳最近的行星(第一个元素).
    3. 打印距离太阳最远的行星(最后一个元素).
    4. 打印金星到天王星之间的行星.
    5. 正向打印所有行星(一行一个)
    6. 反向打印所有行星(一行一个)
"""

list_planets = ["水星", "金星", "地球", "火星", "木星", "土星", "天王星", "海王星"]
print(list_planets[0])
print(list_planets[-1])
print(list_planets[2:-2])
for item in list_planets:
    print(item)
# 反向
# 通过切片实现
for item in list_planets[::-1]:
    print(item)
# 通过索引实现
for i in range(len(list_planets) - 1, -1, -1):
    print(list_planets[i])
