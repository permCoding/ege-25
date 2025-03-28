# f = open('./26_19890-ex.txt')
f = open('./26_19890.txt')
n, g = map(int, f.readline().split())

t = [int(e) for e in f]
v1 = [e for e in t if 310<=e<=320]
v2 = sorted(e for e in t if e>320 or e<310)

sm_v1 = sum(v1)
print(sm_v1, len(v1))
# print(v2)

sm_all = sm_v1
for i in range(len(v2)):
    if sm_all + v2[i] <= g:
        sm_all += v2[i]
    else:
        pos = i
        break
print(sm_all, pos)

mx_sm_all = sm_all
sm_all -= v2[pos]
for i in range(pos+1, len(v2)):
    if sm_all + v2[i] <= g:
        mx_sm_all = sm_all + v2[i]
    else:
        break
print(mx_sm_all)


# 129 10000