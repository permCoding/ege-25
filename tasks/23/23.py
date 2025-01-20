def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a+2,b) + f(a*4,b)

print( f(3,200) * f(200,510) )  # 86



##def sm(x, y):
##    return x + y
##
##print( sm(23, 10) )
