
a=int(input())
l=[i for i in range(1,a-1)]
r=[i for i in range(a-2,0,-1)]
sum=0
for i in range(a-2):
    sum+=l[i]*r[i]

print(sum,3)