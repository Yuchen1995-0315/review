"""
    装饰器 -- 推导过程
    在不改变旧功能(进入后台，删除订单)基础上，为其增加新功能(验证权限)
    练习:exercise07
"""

def verif_permissions(func):
    # 2. * args 为了解决位置实参个数无限问题
    def wrapper(*args,**kwargs):# * 将实参合为一个元组
        # 新功能
        print("验证权限")
        # 旧功能
        # 3. 内部函数的返回值就是旧功能的返回值
        return func(*args,**kwargs)# * 将实参拆分，与形参对应

    return wrapper

# 旧功能
@verif_permissions# enter_background = verif_permissions(enter_background)
def enter_background(login_id,pwd):
    print(login_id,"进入后台")

@verif_permissions
def delete_order():
    print("删除订单")
    return True

# # 拦截  =  新 + 旧
# enter_background = verif_permissions(enter_background)
#
# delete_order = verif_permissions(delete_order)

# 1.调用的是内部函数
enter_background("abc",pwd = "123")
print(delete_order())
