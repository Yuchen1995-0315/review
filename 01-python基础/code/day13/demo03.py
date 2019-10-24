"""
    对象 --> str
    练习：demo02.py
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0.0):
        self.name = name
        self.age = age
        self.score = score

    # 对象 -->  str:对人友好(没有格式限制)
    def __str__(self):
        return "我叫%s,年龄是:%d,成绩是%.1f" % (self.name, self.age, self.score)

    # 对象 -->  str:解释器可识别(格式必须符合python语法)
    def __repr__(self):
        return 'StudentModel("%s",%d,%.1f)' % (self.name, self.age, self.score)


s01 = StudentModel("孙悟空", 27, 100)
# 1. 对象 -->  str(人看)
print(s01)  # <__main__.StudentModel object at 0x7ff62a30d400>

msg = str(s01)  # s01.__str__()
print(msg)

#
# 2. eval作用：将字符串当成python代码执行
print(eval("1+2*5"))
# re = eval('StudentModel("孙悟空",27,100)')

# 对象克隆 eval + repr
# 3. 对象 -->  str(解释器看)
re = eval(repr(s01))  # s01.__repr__()
# re = s01
s01.name = "悟空"
print(re.name)

print(re)
