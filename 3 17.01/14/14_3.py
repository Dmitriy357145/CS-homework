for x in range(1,1001):
    s = 6**2025 + 6**25 - x
    c = 0
    while s>0:
        if s%6==0:
            c +=1
        s//=6
    if c == 2002:
        print(x)
        

