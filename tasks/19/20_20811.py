def step(k): return [ k+1, k+4, k*2 ]


k0 = 24  # __

for k1 in step(k0):
    print()
    print('1', k1, k1<51)
    print()
    for k2 in step(k1):  # 19 = 25
        print('2  ', k2, k2<51)
        
        for k3 in step(k2):
            print('3    ', k3, k3>=51)

        #     for k4 in step(k3):  # 21
        #         print('4      ', k4, k3<=87)
