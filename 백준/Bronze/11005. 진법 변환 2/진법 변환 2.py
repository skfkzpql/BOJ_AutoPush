from  math import *
a, b = map(int,open(0).read().split())
l=[]

c = int(log10(a)/log10(b))

for i in range(0,c+1):
    d = b**(c-i)
    m = a//d
    n = a%d
    a = a-(d*m)
    if m > 9:
        m = chr(m+55)
    l.append(str(m))

print(*l,sep='')

