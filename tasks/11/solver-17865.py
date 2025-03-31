from math import log2, ceil

len_alph = 10 + 52 + 963

n = 257  # кол-во символов в sn
# bit_on_smb = ceil(log2(len_alph))
bit_on_smb = 11
bit_on_sn  = n * bit_on_smb
byte_on_sn = ceil(bit_on_sn / 8)

print(byte_on_sn * 2000)
print(693 * 1024)




# x = 10.001
# print(ceil(x))
# print(floor(x))
