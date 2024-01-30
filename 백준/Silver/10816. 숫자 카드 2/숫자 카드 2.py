import sys

f=sys.stdin.read().splitlines()
a=f[1].split()
b=f[3].split()

s=set(a)
d=dict(zip(s,[0]*len(s)))

for i in a:
    d[i]+=1

for i in b:
    if i in s:
        print(d[i],end=' ')
    else:
        print(0, end=' ')