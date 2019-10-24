# 练习1：在终端中获取一个字符串，循环打印每个字符的编码.
str_input = input("请输入字符串：")
for item in str_input:
    print(ord(item))

# 练习2：在终端中反复录入一个编码值，然后打印字符串。
#       如果录入空字符串，则退出程序。
while True:
    str_input = input("请输入：")
    if str_input == "":
        break

    code_value = int(str_input)
    print(chr(code_value))

