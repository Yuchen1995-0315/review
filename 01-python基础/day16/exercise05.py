"""
    练习3:yield --< MyRange
"""


class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        start_value = 0
        while start_value < self.__stop_value:
            yield start_value
            start_value += 1


for item in MyRange(3):
    print(item)
