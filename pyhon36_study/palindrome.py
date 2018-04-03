# 筛选回数

def is_palindrome(num):

    if 10 > num > 0:
        return True

    numlist = []
    low = num % 10
    while num > 0:
        numlist.append(low)
        num //= 10  # 整除
        low = num % 10

    lens = len(numlist)
    i = 0
    j = lens - 1

    while i < j:
        if numlist[i] != numlist[j]:
            return False
        i += 1
        j -= 1

    return True


output = filter(is_palindrome, range(1, 10000))
print(list(output))
