for n in range(1,100):
    b = bin(n)[2:]
    if (b.count('1') + b.count('0'))%2 == 0:
        for i in len(str(b)):
            if len(str(b))%2 ==0:
                i = len(str(b))//2
            else:
                i = len(str(b))//2 + 1
            b = b[i-1] + b[i] + b[i+1]
    else:
        continue
    r = int(b,2)
    print(n,r)
