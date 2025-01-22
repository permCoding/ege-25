def f(a, b):
    if a == b: return 1
    if a < b or a == 28: return 0
    return f(a-2, b) + f(a//2 if a%2==0 else a-3, b)

print( f(98, 1) )

##a = 13
##print( a//2 if a%2==0 else a-3 )

##a = 14
##if a%2 == 0:
##    a //= 2
##else:
##    a -= 3
##print(a)

# x += 1  # x = x + 1
