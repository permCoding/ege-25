def step(k): return [ k-2, k//2 ]


k0 = 176

for k1 in step(k0):
    print(1, k1, k1>87)
    
    for k2 in step(k1):  # 19
        print(2, k2, k2<=87)
