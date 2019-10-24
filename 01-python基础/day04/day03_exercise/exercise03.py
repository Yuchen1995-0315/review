"""
根据身高体重，参照BMI,返回身体状态。
    BMI：用体重(千克)除以身高(米)的平方。
    体重过低：小于18.5(不包含)
    正常：18.5  -- 24(不包含)
    超重：24  -- 28(不包含)
    I度肥胖：28  -- 30(不包含)
    II度肥胖：30  -- 40(不包含)
    III度肥胖：大于40
    要求：循环不断执行，如果身高是空字符串则退出。
"""
while True:
    height = input("请输入身高(米)：")
    # 短路思想
    if height == "":
        break
    height = float(height)
    weight = float(input("请输入体重(千克)"))
    bmi = weight / height ** 2
    if bmi < 18.5:
        print("体重过低")
    elif bmi < 24:
        print("正常")
    elif bmi < 28:
        print("超重")
    elif bmi < 24:
        print("正常")
    elif bmi < 30:
        print("I度肥胖")
    elif bmi < 40:
        print("II度肥胖")
    else:
        print("III度肥胖")
