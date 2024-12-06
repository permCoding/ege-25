def solve_1():
    A = []
    for x in range(100, 200):
        if ((x in P) <= (((x in Q) and (x not in A)) <= (x not in P))) == False:
            A.append(x)
    print(A[-1]-A[0], A)
    

def solve_2():
    def f(A, x):
        return (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))
    res = []
    for l in range(100, 200):
        for r in range(l+1, 200):
            A = list(range(l, r+1))
            if all(f(A, x) for x in range(100, 200)):
                res.append(len(A)-1)  # это точки, а -1 это расстояние между точками
    print(min(res))
    
P = list(range(130, 172))
Q = list(range(150, 186))

solve_1()
solve_2()
