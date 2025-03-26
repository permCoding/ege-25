import math

for n in range(1, 1_000):
    alph = 10 + 52 + 963  # 1025
    bit_per_smb = 11

    bytes_per_sn = math.ceil(n * bit_per_smb / 8)

    if 2_000 * bytes_per_sn >= 693 * 1024:
        print(n-1)
        break



"""
x = 9.06
print(round(x))
print(math.floor(x))
print(math.ceil(x))
"""