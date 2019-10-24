from time import sleep
from threading import Thread,Lock

# 账户类
class Account:
    def __init__(self,id,balance,lock):
        self.id = id   # 账户名
        self.balance = balance # 存款
        self.lock = lock # 锁

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount

    # 存钱
    def deposit(self,amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance

# 两个账户
Tom = Account('Tom',5000,Lock())
Alex = Account('Alex',8000,Lock())

# 转账
def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount) # from_钱减少
        sleep(0.1)
        # 两个线程都阻塞在to上锁位置
        if to.lock.acquire():
            to.deposit(amount) # to 钱增加
            to.lock.release()
        from_.lock.release()
    print("%s给%s转了%d"%(from_.id,to.id,amount))

t1 = Thread(target = transfer,args=(Tom,Alex,2000))
t2 = Thread(target = transfer,args=(Alex,Tom,1800))
t1.start()
t2.start()
t1.join()
t2.join()





