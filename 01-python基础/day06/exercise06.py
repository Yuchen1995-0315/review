"""
    打印图形：
    * * * *
    # # # #
    * * * *
    # # # #
    * * * *
"""
for r in range(5):
    for c in range(4):
        if r % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()  # 换行
