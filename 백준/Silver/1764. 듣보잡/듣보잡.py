import sys

a,b,*l=sys.stdin.read().rsplit()
a,b=map(int,[a,b])

c={*l[:a]}
d={*l[a:]}
e=c.intersection(d)
e=sorted(list(e))
print(len(e),*e,sep='\n')
