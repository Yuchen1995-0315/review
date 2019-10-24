"""
    复习
        time --> 时间戳(1970 1 1)   时间元组(年月日...)
                 看文档
        异常处理
            现象：程序不再向下执行，而是返回给调用者.
            处理目的：让错误(异常 / 向上)状态改为正常(向下)状态
            处理手段：
                try:
                    可能出错的代码:
                except 错误类型:
                    处理逻辑

                try:
                    可能出错的代码:
                finally:
                    必须完成的任务

                try:
                    可能出错的代码:
                except 错误类型:
                    出错的处理逻辑
                else:
                    没出错的逻辑
            人为抛出异常：
                raise 异常对象
                为了快速/简单的传递错误信息(避免层层return)

        迭代：在上一次结果的基础上重复.
            for item in 容器：
                print(item)

            1. 获取迭代器对象
            iterator = 容器.__iter__()
            2. 通过迭代器对象获取下一个元素
            while True:
                try:
                    item = iterator.__next__()
                    print(item)
                3. 如果停止迭代则退出循环
                except StopIteration:
                    break




"""