import math

n = 257
alph = 10 + 52 + 963  # 1025
bit_per_smb = 11

bytes_per_sn = math.ceil(n * bit_per_smb / 8)

print(2_000 * bytes_per_sn)
print(693 * 1024)



"""
x = 9.06
print(round(x))
print(math.floor(x))
print(math.ceil(x))
"""