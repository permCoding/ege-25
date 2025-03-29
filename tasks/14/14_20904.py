def get(x):
    n = 3**100 - x
    r = ''
    while n > 0:
        r = str(n%3) + r
        n //= 3
    return r

for x in range(2030, 0, -1):
    if get(x).count('0') == 1:
        print(x)  # 1823
        break