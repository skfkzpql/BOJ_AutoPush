import sys
a=sys.stdin.read().rstrip()
l=[]
r=len(a)
for i in range(r):
    for j in range(r-i):
        l.append(a[j:j+i+1])

s=set(l)
print(len(s))