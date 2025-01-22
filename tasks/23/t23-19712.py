def f(a, b, way):
    if '111' in way or '222' in way: return 0
    if a < b: return 0
    if a == b: return 1
    #
    #
    #
    #
    return f(a-2, b, way+'1') + f(a-7, b, way+'2')

print( f(40, 1, '') )


##way = '112111'
##way = '122212'
# Если число четное, Разделить на 2, Иначе Вычесть 7
