import sys
a=sys.stdin.read().rsplit()
n=int(a[0])
m=int(a[1])
l=a[2:2+n]
d=dict(zip(a[2:2+n],range(1,n+1)))
for i in a[-m:]:
    if i.isdigit():
        print(l[int(i)-1])
    else:
        print(d[i])