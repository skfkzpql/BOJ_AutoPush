from collections import Counter

l = open(0).read().rstrip().splitlines()
n, m = map(int,l[0].split())

l = [i for i in l[1:] if len(i)>=m]

d = Counter(l)
s = list(zip( d.values(),[len(i) for i in d.keys()],d.keys()))

print(*[i[2] for i in sorted(s, key=lambda x: (-x[0],-x[1],x[2]))], sep='\n')