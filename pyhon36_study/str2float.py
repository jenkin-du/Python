# 将字符串转化成float型数字
# 这是改过的版本
from functools import reduce

NumMap = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}


def fn(x, y):
    return x * 10 + y


def char2num(char):
    return NumMap[char]


def str2float(string):
    numList = list(map(char2num, string))
    n = 0  # 记录小数位数

    for i in numList:
        if i != '.':
            n += 1
        else:
            break
    lens = len(numList) - n - 1
    numList.remove('.')
    i = 1
    m = 1
    while i <= lens:
        m *= 10
        i += 1

    return reduce(fn, numList) / m


result = str2float('2234.456')
print(result)
