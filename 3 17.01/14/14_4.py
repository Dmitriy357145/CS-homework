for x in range(1,801):
    s = 7**1040 + 7**40 - x
    c = 0
    while s>0:
        if s%7==0:
            c += 1
        s//=7
    if c==1002:
        print(x)
