def f(n):
    return (abs(n)%10 == 3) and (99 < abs(n) < 1000)

t = [int(s) for s in open('./17_17636.txt')]  # 1

mx3 = max(num for num in t if f(num))  # 2

lst = []  # 3
for i in range(len(t)-2):
    s = t[i:i+3]
    u1 = any(f(n) for n in s)
    u2 = sum(s) < mx3
    if u1 and u2:
        lst.append(t[i]+t[i+1]+t[i+2])
    
print(len(lst), max(lst))  # 147 944

"""
элементы по модулю не превышают 100000 включительно. 

Определите количество троек элементов последовательности, в которых 

a) хотя бы один элемент оканчивается на 3 и является трёхзначным числом, 

b) а сумма всех элементов меньше максимального элемента последовательности, 
оканчивающегося на 3 и являющегося трёхзначным числом 

количество найденных троек, затем максимальную из сумм элементов таких троек
"""