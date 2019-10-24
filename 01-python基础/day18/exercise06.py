"""
    在不改变旧功能(进入后台，删除订单)基础上，为其增加新功能(验证权限)
"""
def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)
    return wrapper

@verif_permissions
def enter_background():
    print("进入后台")

@verif_permissions
def delete_order():
    print("删除订单")

enter_background()
delete_order()