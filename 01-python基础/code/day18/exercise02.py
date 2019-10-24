# 练习1:在3男，4女中，选出2个人的所有可能性.
# ("男1号","男2号","男3号")
# ("女1号","女2号","女3号","女4号")
import itertools

tuple_man = ("男1号", "男2号", "男3号")
tuple_woman = ("女1号", "女2号", "女3号", "女4号")
result = tuple(itertools.product(tuple_man,tuple_woman))
print(len(result),result)