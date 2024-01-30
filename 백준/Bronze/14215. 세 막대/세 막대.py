l=list(map(int,input().split()))
l.append(max(l))
l.remove(max(l))
if l[2] >= sum(l[0:2]):
    l[2]=sum(l[0:2])-1
print(sum(l))