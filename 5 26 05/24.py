s = open('24.txt').readline()
m=0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c = s[l:r+1]
        k =c.count('UPIT')
        if k==80:
            m = max(m,len(c))
        if k<80:
            continue
        if k>80: break
print(m)
