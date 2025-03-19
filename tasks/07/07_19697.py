# audio

# S = V * T
# T = S / V

# 19697

n = 18
w = 1 * n * 64_000
S = w * 68  # bit
V = 204_000  # bit/sec
print(S / V)
