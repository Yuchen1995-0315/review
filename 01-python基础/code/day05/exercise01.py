"""
    练习1：在终端中循环录入学生的成绩,
          如果录入空字符串,则停止。
          打印最高分、最低分、平均分。
"""
list_score = []
while True:
    str_score = input("请输入学生成绩：")
    if str_score == "":
        break

    list_score.append(float(str_score))

print(max(list_score))
print(min(list_score))
print(sum(list_score) / len(list_score))
