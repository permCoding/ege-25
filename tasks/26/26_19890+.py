# f = open('./26_19890-ex.txt')
f = open('./26_19890.txt')
n, g = map(int, f.readline().split())

t = [int(e) for e in f]
v1 = [e for e in t if 310<=e<=320]
v2 = sorted(e for e in t if e>320 or e<310)
v = v1 + v2

sm = 0
for i in range(len(v)):
    if sm + v[i] <= g:
        sm += v[i]
    else:
        pos = i
        break
print(sm, pos)

sm -= v[pos-1]
for i in range(len(v)-1, pos, -1):
    if sm + v[i] <= g:
        print(sm + v[i])
        break

# 129 10000