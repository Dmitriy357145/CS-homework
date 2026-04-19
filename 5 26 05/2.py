from itertools import *
def u(w,y,x,z): return ((x or y)<=(y and z)) and w
print(*{''.join(p) for p in permutations('xyzw')
        for a,b,c,d in product(*[[0,1]]*4)
        if 3==sum(u(**dict(zip(p,r)))==1 for r in
                  {(1,1,a,0),(1,1,1,0),(0,b,c,d)})})
        
