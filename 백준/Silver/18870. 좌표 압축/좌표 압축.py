import sys
a,*l=map(int,sys.stdin.read().rsplit())

b=dict(zip(sorted(set(l)),[i for i in range(a)]))

for i in l:
    print(b[i],end=' ')