# 72600 - https://inf-ege.sdamgia.ru/problem?id=72600
def f(x):
    return (x in Q) <= ((x not in P) <= (((x not in R) and (x not in A)) <= (x not in Q)))

P = list(range(7, 64))
Q = list(range(28, 100))
R = list(range(85, 120))

A = []
for x in range(1, 200):
    if f(x) == False:
        A.append(x)
print(len(A)-1, A)  # =20 ? на сайте =22
