for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (w <= (not(z <= x))) or y
                if F == False:
                    print(z, x, y, w)
