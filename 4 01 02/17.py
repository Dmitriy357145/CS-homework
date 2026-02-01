a  = [int(x) for x in open('17.txt')]
mi = min([x for x in a if 100<=abs(x)<1000])
mx  = max([x for x in a if 100<=abs(x)<1000])
def check(n):
    return 100<=abs(n)<1000
ans = []
for x,y,z in zip(a,a[1:],a[2:]):
    if (100<=abs(x)<1000)+(100<=abs(y)<1000)+(100<=abs(z)<1000)>=2 and \
       x+y+z>mx+mi:
        ans.append(x+y+z)
print(len(ans),max(ans))
