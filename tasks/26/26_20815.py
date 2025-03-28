# f = open('./26_20815-ex.txt')
f = open('./26_20815.txt')
n, k = map(int, f.readline().split())

pers = []
for line in f:
    t = list(map(int, line.split()))
    p = [t[1]+t[2]+t[3]+t[4], t[4], t[0]]
    pers.append(p)

pers.sort(key=lambda x: (-x[0], -x[1], x[2]))

for p in pers: print(p)

ball_k = pers[k-1][0]
print(ball_k)

ppb = ball_k if pers[k][0] == pers[k-1][0] else 0
print(ppb)

cnt_ppb = sum(1 for p in pers if p[0] == ppb)
print(cnt_ppb)

for i in range(k-1, -1, -1):
    if pers[i][0] != ppb:
        print(pers[i][2])
        break
# 45539 127