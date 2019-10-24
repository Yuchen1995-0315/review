# 练习:在终端中循环录入字符串，如果录入空字符，则停止录入.
#      最后打印录入的内容（一个字符串）

list_result = []
while True:
    str_input = input("请输入内容：")
    if str_input == "":
        break
    list_result.append(str_input)

str_result = "".join(list_result)
print(str_result)
