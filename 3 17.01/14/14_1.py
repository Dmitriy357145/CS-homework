
for x in range(1,5770):
    s = 9**2025 + 9**1000 - x
    c = 0
    while s>0:
        if s%9==0:
            c +=1
        s//=9
    if c == 1026:
        print(x)
        
