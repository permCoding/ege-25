t = [int(s) for s in open('./17_17873.txt')]  # 1

mn = min(t)  # 2

cnt, mx = 0, 0  # 3
for i in range(len(t)-1):
    if t[i]%16 == mn or t[i+1]%16 == mn:
        cnt += 1
        mx = max(mx, t[i]+t[i+1])

print(cnt, mx)

# t = [7,18,55,55,12,34]
# mn = 2

"""
количество пар, в которых 
остаток от деления хотя бы одного из элементов на 16 
равен минимальному элементу 

В ответе запишите количество найденных пар, 
затем максимальную из сумм элементов таких пар.

"""



"""
количество нечётных
количество пар с нечётной суммой
пару с маскимальной нечётной суммой
кол-во пар с одинаковыми числами
кол-во пар где первое число больше второго
кол-во пар с одинаковой нечётностью/чётностью
"""