def newfunc(*args):
    x = 1
    p = [x**i for i in args]
    return p
print newfunc(1,2,3)