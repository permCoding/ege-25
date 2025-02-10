for n in range(10, 60):
    b = bin(n)[2:]
    if n%2 == 0:
        b += '100'
    else:
        b += '011'
    r = int(b, 2)
    print(r, n)  # 308 38
