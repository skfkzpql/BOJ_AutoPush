import sys
n,m,*s=map(int,sys.stdin.read().rstrip().split())
a = [0]*m
b = [0]*m
count=0

for i in s[:n]:
    a[i-1]+=1
for j in s[-n:]:
    b[j-1]+=1
for k in range(m):
    count+=a[k]*b[k]
print(n**2 -count)