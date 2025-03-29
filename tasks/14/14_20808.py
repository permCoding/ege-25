def get(x):
    n = v - x
    r = ''
    while n > 0:
        r = str(n%7) + r
        n //= 7
    return r

v = 7**170 + 7**100
mx_cnt = 0
mx_x = 0
for x in range(1, 2031):
    cnt = get(x).count('0')
    # print(x, '\t', cnt)
    if cnt >= mx_cnt:
        mx_cnt = cnt
        mx_x = x

print(mx_x)  # 1715
