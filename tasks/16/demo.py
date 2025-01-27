import sys

sys.setrecursionlimit(2222)
sys.set_int_max_str_digits(55000)

def F(n):
    if n == 1:
        return 1
    else:
        return (n-1) * F(n-1)

print( (F(2024) + 2*F(2023)) / F(2022))
print(2022*2025)

# 4094550
