import sys
a=int(sys.stdin.readline().rstrip())
l={}
for _ in range(a):
    b = int(sys.stdin.readline().rstrip())
    if b not in l:
        l[b]=1
    else:
        l[b]+=1

d=list(l.keys())
d.sort()
for i in d:
    for j in range(l[i]):
        print(i)