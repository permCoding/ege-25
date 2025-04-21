def step(p):
    h, a, b, sm = p
    return [
        (h+1, a+1, b, a+1+b), 
        (h+1, a, b+1, a+b+1), 
        (h+1, a*2, b, a*2+b), 
        (h+1, a, b*2, a+b*2)]


s = 23
p0 = (0, 5, s, 5+s)
t1 = step(p0)
if all(p1[3]<=59 for p1 in t1):
    print(p0, t1)
    for p1 in t1:
        t2 = step(p1)
        if all(p2[3]<=59 for p2 in t2):
            print(p1, sorted(t2, key=lambda x: x[3]))
        
        
