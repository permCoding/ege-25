def f(A, x):
    return (x%A!=0) <= ((x%6==0) <= (x%4!=0))
A = 500
while A > 0:
    if all(f(A,x) for x in range(500)):
        print(A)
        break
    A -= 1