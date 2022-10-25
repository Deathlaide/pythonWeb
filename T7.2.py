def cache(number):
    cacheValue=dict()
    def func(value, count = 1):
        if value not in cacheValue or cacheValue[value][1] <= 0:
            print("Caching")
            cacheValue[value]=[number(value),count]
            cacheValue[value][1] -= 1
        else:
            print("Not caching")
            cacheValue[value][1] -= 1
    return func

@cache
def init(i):
    return i

init(1, 4)
init(1)
init(1)
init(1)
init(1)

init(6, 2)
init(6)

init(8)
init(10)

