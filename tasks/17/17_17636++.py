t = [int(s) for s in open('./17_17636.txt')]  # 1

mx3 = max(num for num in t if (abs(num)%10 == 3) and (99 < abs(num) < 1000))  # 2

lst = []  # 3
for i in range(len(t)-2):
    e1 = (abs(t[i])%10 == 3) and (99 < abs(t[i]) < 1000)
    e2 = (abs(t[i+1])%10 == 3) and (99 < abs(t[i+1]) < 1000)
    e3 = (abs(t[i+2])%10 == 3) and (99 < abs(t[i+2]) < 1000)
    u1 = e1 or e2 or e3
    u2 = (t[i]+t[i+1]+t[i+2]) < mx3
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