s = '230'
base = 8
dec = 0

p = len(s)  # 8
for smb in s:
    p -= 1
    dec += int(smb) * base**p

print(dec)


"""
230(8) => 152(10)
1011(2) => X(10)
3210
8421
1*2**3 + 0*2**2 + 1*2**1 + 1*2**0 = 

0   0  0  0  0 0 0 0
1   1  1  1  1 1 1 1
7   6  5  4  3 2 1 0
128 64 32 16 8 4 2 1

0

255

1001 => 9(10)
18(10) => 10010(2)
10101(2) => 21(10)
24(10) => 11000(2)
25(10) => 11001(2)

"""