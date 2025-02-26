for n in range(4, 10_000):
    
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        
        if '12' in s:
            s = s.replace('12','2',1)
        if '322' in s:
            s = s.replace('322','21',1)
        if '222' in s:
            s = s.replace('222','3',1)

    if sum(int(e) for e in s) == 15:  # сумма цифр в строке
        print(n)
        break

""" 05
for n in range(1, 1_000):
    
    b = bin(n)[2:]
    if n%2 == 0:
        b += '01'
    else:
        b = '1' + b + '1'
    r = int(b, 2)
    
    if r > 156:
        print(n)
        break



s = '1222'

print(s.find('13') > -1)
print('12' in s)
print('13' in s)


s = ' 12 34343 12 000'
# s = s.replace('12', '*')  # все вхождения
s = s.replace('12', '*', 1)  # все вхождения
print(s)


s = '123005'
print( sum( int(e) for e in s ) )

sm = 0
for e in s:
    sm += int(e)
print(sm)

sm = 0
for i in range(len(s)):
    sm += int(s[i])
print(sm)
"""