"""
    练习：
        一张纸的厚度是0.01毫米
        请计算，对折多少次超过珠穆朗玛峰(8844.43米).
"""

# thickness = 0.01 / 1000
thickness = 1e-5
count = 0
while thickness < 8844.43:
    # 对折
    thickness *= 2
    count += 1

print(count)

