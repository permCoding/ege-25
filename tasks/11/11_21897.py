from math import ceil

k = 3  # бит на символ => 8
n = 246  # символов в sn
sn = ceil(k * n / 8)  # байт на sn

print(sn * 703_569)
print(77 * 1024 * 1024)
