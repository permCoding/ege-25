"""
    унарная
not   НЕ - отрицание

    бинарные
and   И - и тот и тот
or    ИЛИ - или тот или тот или оба вместе
^ XOR   исключающее ИЛИ - ЛИБО - либо тот либо этот, но никак не вместе
imp <= 
"""

# for x in 0, 1:
#     print(x, int(not(x)))
    
# for x in 0, 1:
#     for y in 0, 1:
#         print(x, y, x and y)

# for x in 0, 1:
#     for y in 0, 1:
#         print(x, y, x or y)

for x in 0, 1:
    for y in 0, 1:
        print(x, y, x ^ y)
