# f = open('./20910-ex.txt')
f = open('./26_20910.txt')
n, m, k = map(int, f.readline().split())

cols = [m] * (k+1)
for line in f:
    row, col = map(int, line.split())
    cols[col] = min(cols[col], row)

pairs = [min(cols[col], cols[col+1]) - 1 for col in range(1, k)]
max_row = max(pairs)
print(max_row)

for col in range(1, k):
    if min(cols[col], cols[col+1]) - 1 == max_row:
        print(col)
