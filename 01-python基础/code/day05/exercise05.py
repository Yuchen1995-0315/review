# 练习:将英文语句，进行单词反转(结果还是str).
# "How are you"  --> you are How

str_message = "How are you"
list_temp = str_message.split(" ")
str_result = " ".join(list_temp[::-1])
print(str_result)




