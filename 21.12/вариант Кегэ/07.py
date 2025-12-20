S = 3072*4096*24*150
V = 4* (2**23)
S_sj = S*0.5
t_sj = 0.1*150
t_per_sj = S_sj / V
A = t_sj + t_per_sj
t_per = S/V
B = t_per
print(A)
print(B)
