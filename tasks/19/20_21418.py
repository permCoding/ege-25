def step(k): return [ k-2, k//2 ]


k0 = 179  # 178 179

for k1 in step(k0):
    print()
    print('1', k1, k1>87)
    
    for k2 in step(k1):
        print('2  ', k2, k2>87)
        
        for k3 in step(k2):  # 20
            print('3    ', k3, k3<=87)
