for x in range(1,2736):
    s = 5**2025 + 5**1500 - x
    c = 0
    while s>0:
        if s%5==0:
            c +=1
        s//=5
    if c == 527:
        print(x)
        

