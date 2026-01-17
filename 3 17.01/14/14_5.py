from string import *
for x in printable[:23]:
    s = int(f'1{x}1{x}1{x}1{x}1',23) + int(f'20{x}24',23) + int(f'1{x}235',23)
    if s%22==0:
        print(x,s//22)
