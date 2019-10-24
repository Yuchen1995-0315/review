"""
    练习:
        公式：
            距离 = 加速度 * 时间的平方 * 0.5 + 初速度 × 时间
        已知(在终端中录入)：距离、时间、初速度
        计算：加速度

        (距离 - 初速度 × 时间) * 2/ 时间的平方  = 加速度
"""
distance = float(input("请输入距离："))
initial_velocity = float(input("请输入初速度："))
time = float(input("请输入时间："))
accelerated_speed = (distance - initial_velocity * time) * 2 / time ** 2
print("加速度是：" + str(accelerated_speed))# round(accelerated_speed,2)


