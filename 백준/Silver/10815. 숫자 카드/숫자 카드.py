import sys
f=list(map(int,sys.stdin.read().rsplit()))
s=set(f[1:f[0]+2])
l=f[-f[f[0]+1]::]

for i in l:
    print('01'[i in s],end=' ' )