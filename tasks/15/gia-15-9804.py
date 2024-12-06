def f(A, x):
    return (x&29!=0) <= ((x&17==0) <= (x&A!=0))
A = 0
while A < 200:
    if all(f(A,x) for x in range(200)):
        print(A)
        break
    A += 1