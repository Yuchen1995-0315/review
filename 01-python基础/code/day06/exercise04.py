# 练习1:["无忌","张翠山","张三丰"]-->{"无忌":2,"张翠山":3,"张三丰":3}
#       key: 列表元素, value: key的长度
list_names = ["无忌", "张翠山", "张三丰"]
dict_names = {item: len(item) for item in list_names}
print(dict_names)

# 练习2:姓名列表： ["无忌","赵敏","周芷若"]
#      房间号：[101,102,103]
#      将两个列表合并为字典,key:姓名列表元素,值:房间列表元素.

list_names = ["无忌", "赵敏", "周芷若"]
list_rooms = [101, 101, 103]
dict_info = {list_names[i]: list_rooms[i] for i in range(len(list_names))}
print(dict_info)

# 需求：根据房间号查找人
#      根据值找键

# 方法1:遍历字典所有记录，判断值.
# 方法2:反转key 与 value
# dict_info = {v:k for k,v in dict_info.items() }
# print(dict_info)

# 注意：反转后，因为键不能相同，所以可能导致丢失数据。
list_info = [(v,k) for k,v in dict_info.items()]
print(list_info)
# 15:37













