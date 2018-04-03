def odd_iter():
    num = 1

    while True:
        num += 2
        yield num


def not_visiable(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()
    while True:
        num = next(it)
        yield num
        it = filter(not_visiable(num), it)


for n in primes():
    if n < 1000:
        print(n, end=',')
    else:
        break
