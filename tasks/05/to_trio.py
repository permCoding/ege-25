n = 1327
t = ''

while n > 0:
    t = str(n%3) + t
    n //= 3

print(t)
