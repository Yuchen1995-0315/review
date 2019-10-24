"""
    字符串字面值
    练习:exercise06
"""

# 1. 各种引号
str01 = "悟空"
str02 = '悟空'

# 可见即所得
str03 = """
    悟
       空
"""
print(str03)
str04 = '''悟空'''

str05 = '我叫"孙悟空"'
str05 = "我叫'孙悟空'"

print(str05)

# 2.转义符：改变原始字符含义的特殊符号
# \"   \'   \\    \n 换行   \t
str06 = "我叫\'孙\n悟\t空\""
print(str06)

url = "C:\\nltk_data\corpora\\biocreative_ppi"
# 原始字符串（没有 转义符）
url = r"C:\nltk_dat\a\corpora\biocre\ative_ppi"
print(url)

# 3. 格式化
name = "悟空"
age = 3000
score = 99.99
print("%s的年龄是%d成绩是%.1f。"%(name,age,score))














