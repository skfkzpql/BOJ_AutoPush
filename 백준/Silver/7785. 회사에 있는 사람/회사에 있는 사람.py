a=open(0).read().split()

d=dict(zip(a[1::2],a[2::2]))
l=[]
for i,j in d.items():
    if j=='enter':
        l.append(i)

print(*sorted(l,reverse=True),sep='\n')
    