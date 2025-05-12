k = 8  # бит на пиксель

r = 1280 * 960 * k  # 1 photo in bit
p = r * 24  # размер пакета in bit

v = 1_392_640  # bit/sec
t = 180  # sec

print(p)
print(v * t)
