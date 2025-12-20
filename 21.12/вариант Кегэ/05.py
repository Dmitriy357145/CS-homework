for n in range(1,100):
    b = bin(n)[2:]
    if n%4==0:
        b = b + b[-2:]
    else: b = b + bin(n%4)[2:]
    r = int(b,2)
    if r > 250:
        
        print(n,r)
        break
