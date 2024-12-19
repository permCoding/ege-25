def f(n, way=[]):
    if n == stop: 
        print(way)
        return 1
    if n < stop: return 0
    w1 = f(n-2, way+['-2'])
    w2 = f(n//2, way+['//2'])
    return w1 + w2

stop = 16
print(f(38))
