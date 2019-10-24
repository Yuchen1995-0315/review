"""
    可迭代对象常用工具
"""


class IterableHelper:
    """
        可迭代对象助手
    """

    # 静态方法：函数(不需要操作实例/类数据) --> 方法
    @staticmethod  # 为了不隐式(自动)传参(self/cls)
    def find_all(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件搜索全部元素.
        :param iterable_target:需要搜索的可迭代对象
        :param func_condition:需要判断的条件
        :return:生成器对象,存储满足条件的结果.
        """
        for item in iterable_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件搜索单个元素.
        :param iterable_target:需要搜索的可迭代对象
        :param func_condition:需要判断的条件
        :return:满足条件的结果.
        """
        for item in iterable_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable_target, func_condition):
        """
            在可迭代对象中，查找满足条件的数量.
        :param iterable_target:需要搜索的可迭代对象
        :param func_condition:需要判断的条件
        :return:int类型,满足条件的数量.
        """
        count = 0
        for item in iterable_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def sum(iterable_target, func_handle):
        """
            在可迭代对象中，根据指定逻辑累加其中的元素.
        :param iterable_target:需要累加的数据(可迭代对象)
        :param func_condition:需要累加的逻辑(方法/函数)
        :return:累加结果
        """
        sum_value = 0
        for item in iterable_target:
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def is_exists(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件判断是否存在元素.
        :param iterable_target:需要搜索的数据(可迭代对象)
        :param func_condition:需要判断的条件(方法/函数)
        :return:是否存在(bool类型)。
        """
        for item in iterable_target:
            # if item.atk > 50:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def get_max(iterable_target, func_handle):
        """
            在可迭代对象中，根据指定条件查找最大元素
        :param iterable_target:需要搜索的数据(可迭代对象)
        :param func_condition:需要判断的条件(方法/函数)
        :return:最大的元素
        """
        max = iterable_target[0]
        for i in range(1, len(iterable_target)):
            # if max.atk < iterable_target[i].atk:
            if func_handle(max) < func_handle(iterable_target[i]):
                max = iterable_target[i]
        return max

    @staticmethod
    def select(iterable_target, func_handle):
        """
              在可迭代对象中，根据指定逻辑映射元素
          :param iterable_target:需要搜索的数据(可迭代对象)
          :param func_condition:需要处理的逻辑(方法/函数)
          :return:
          """
        # result = []
        # for item in iterable_target:
        #     # result.append( (item.name,item.atk))
        #     result.append(func_handle(item))
        # return result

        for item in iterable_target:
            yield func_handle(item)

    @staticmethod
    def order_by(iterable_target, func_condition):
        for r in range(len(iterable_target) - 1):
            for c in range(r + 1, len(iterable_target)):
                # if iterable_target[r].atk > iterable_target[c].atk:
                if func_condition(iterable_target[r]) > func_condition(iterable_target[c]):
                    iterable_target[r], iterable_target[c] = iterable_target[c], iterable_target[r]

    # 在可迭代对象中，根据指定条件查找最小元素get_min
    @staticmethod
    def get_min(iterable_target, func_condition):
        min_value = iterable_target[0]
        for i in range(1, len(iterable_target)):
            # if min_value.atk > iterable_target[i].atk:
            if func_condition(min_value) > func_condition(iterable_target[i]):
                min_value = iterable_target[i]
        return min_value

    # 根据指定条件对可迭代对象进行降序排列order_by_descending
    @staticmethod
    def order_by_descending(iterable_target, func_condition):
        for r in range(len(iterable_target) - 1):
            for c in range(r + 1, len(iterable_target)):
                if func_condition(iterable_target[r]) < func_condition(iterable_target[c]):
                    iterable_target[r], iterable_target[c] = iterable_target[c], iterable_target[r]

    # 在可迭代对象中，根据指定条件删除元素delete_all
    @staticmethod
    def delete_all(iterable_target,func_condition):
        # [w01,w02,w03]
        for i in range(len(iterable_target)-1,-1,-1):
            # if iterable_target[i].weight < 40:
            if func_condition(iterable_target[i]):
                del iterable_target[i]















