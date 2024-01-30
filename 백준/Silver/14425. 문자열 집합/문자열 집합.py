a,b,*l=open(0).read().split()
a=int(a)
print(sum(x in l[:a]for x in l[a:]))