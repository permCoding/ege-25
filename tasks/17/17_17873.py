t = [int(s) for s in open('./17_17873.txt')]
mn = min(t)

cnt = 0
for i in range(len(t)-1):
    if t[i]%16 == mn or t[i+1]%16 == mn:
        cnt += 1
print(cnt)

# t = [7,18,55,55,12,34]
# mn = 2
