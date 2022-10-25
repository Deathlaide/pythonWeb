def cache(number):
    cacheValue= dict()
    def func(*value):
        if value not in cacheValue:
            print("Caching")
            cacheValue[value] = number(*value)
        else:
            print("Not caching")
        return cacheValue[value]
    return func

@cache
def init(i):
    return i

init(1)
init(2)
init(2)
init(3)
init(4)
init(4)
init(5)
init(6)
init(1)
init(7)
init(8)