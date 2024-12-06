def solve_1():
    A = list(range(10, 30))
    for x in range(10, 30):
        if (((x in A) <= (x in P)) or (x in Q)) == False:
            A.remove(x)
    print(A[-1]-A[0], A)
    

def solve_2():
    def f(A, x):
        return ((x in A) <= (x in P)) or (x in Q)
    res = []
    for l in range(10, 30):
        for r in range(l+1, 30):
            A = list(range(l, r+1))
            if all(f(A, x) for x in range(10, 30)):
                res.append(len(A)-1)  # это точки, а -1 это расстояние между точками
    print(min(res))
    
P = list(range(10, 30))
Q = list(range(13, 19))

solve_1()
solve_2()
