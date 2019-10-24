"""
温度转换器：
    摄氏度 = （华氏度 - 32） 除以 1.8
    开氏度 = 摄氏度 + 273.15
    (1)在终端中录入华氏度，计算摄氏度
    (2)在终端中录入摄氏度，计算开氏度
"""
# (1)在终端中录入华氏度，计算摄氏度
fahrenheit_degree = float(input("请输入华氏度"))
centigrade_degree = (fahrenheit_degree - 32) / 1.8
print("摄氏度是：" + str(centigrade_degree))

# (2)在终端中录入摄氏度，计算开氏度
centigrade_degree = float(input("请输入摄氏度"))
kelvin_degree = centigrade_degree + 273.15
print("开氏度是：" + str(kelvin_degree))