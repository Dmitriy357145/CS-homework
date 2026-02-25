a = [int(x) for x in open('17var05.txt')]
ans = []
mi = min(a)
def f(x):
    return x%27==mi
for x,y in zip(a,a[1:]):
    if f(x)+f(y)>=1:
        ans.append(x+y)
print(len(ans),max(ans))
