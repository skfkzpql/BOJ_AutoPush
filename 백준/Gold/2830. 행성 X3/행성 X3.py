N,*l=map(int,open(0).read().split())
print(sum((d:=sum(i>>j&1 for i in l))*(N-d)*(1<<j)for j in range(20)))