"""
    docs.python.org/zh-cn/3.7

    str01 = " 校训是： 自强 不息,厚 德载物.  "
    -- 查找空格数量
    -- 删除字符串前后空格
    -- 删除所有空格
    -- 查找"自强"的位置
    温馨提示:先看str_method.docx文档,自学str函数。
"""
str01 = " 校训是： 自强 不息,厚 德载物.  "
print(str01.count(" "))
# print(str01.lstrip().rstrip())
print(str01.strip())
print(str01.replace(" ",""))
print(str01.index("自强"))