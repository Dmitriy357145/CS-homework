for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z<=y) and ((not y) == x)) <= (not w))==False:
                    print(x,y,z,w)
