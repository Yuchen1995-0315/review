# 练习: 调用函数
# 万能参数:(位置/关键字)参数无限
def fun08(*args, **kwargs):
    print(args)
    print(kwargs)


fun08()
fun08(1, 23, 4)
fun08(a=1, b=2)
fun08(1, 2, a=1, b=2)
# fun08(1,a=1,2,b=2)
