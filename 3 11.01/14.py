f = []
for x in range(1,1951):
    
    c = 0
    a = 72070 + 7400 - x
    while a>0:
        if a%9==0:
            c+= 1
        a//=9
    f.append(c)
print(max(f))
