def step(k): return [ k-2, k//2 ]


k0 = 180  # 178 179

for k1 in step(k0):
    print()
    print('1', k1, k1>87)
    print()
    for k2 in step(k1):
        print('2  ', k2, k2<=87)
        
        for k3 in step(k2):
            print('3    ', k3, k3>87)

            for k4 in step(k3):  # 21
                print('4      ', k4, k3<=87)
