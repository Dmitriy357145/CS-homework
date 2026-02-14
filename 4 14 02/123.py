s = 18 *  7**108 - 5 * 49**76 + 343**35 - 50
x = 0
s = abs(s)
while s>0:
    x+= s%49
    s//=49
print(x)
