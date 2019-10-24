"""
    list --> str
    练习:exercise04.py
"""

# 需求: 根据某些逻辑，拼接字符串.
# 0123456789
# str_result = ""
# for item in range(10):
#     # 两个字符串拼接，会产生新的字符串对象，
#     str_result = str_result + str(item)
# print(str_result)

list_result = []
for item in range(10):
    # 将新字符串追加到列表中，不会产生新对象
    list_result.append(str(item))
str_result = "".join(list_result)
print(str_result)
