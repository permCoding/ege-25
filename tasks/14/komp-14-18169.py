def get_count(x):
    cnt = 0
    while x > 0:
        ost = x%3
        x = x//3
        if ost == 2: cnt += 1
    return cnt

x = 0
while True:
    x += 1
    f = 3**2000 + 3**10 - x
    r = get_count(f)
    if x%500 == 0:
        print(x, r)
    if r == 2000:
        print(x, r)  # 59050 2000
        break

# это сложная задача - 2 минуты вычисляет