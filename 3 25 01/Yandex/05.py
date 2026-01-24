for n in range(1,100):
    b = bin(n)[2:]
    if n%2==0:
        b = b +  '0'*b.count('0')
    else:
        b  = '1'*b.count('1')  + b
    r  =  int(b,2)
    if r>2000:
        print(n,r)
        
