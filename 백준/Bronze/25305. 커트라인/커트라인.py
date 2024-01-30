import sys

a,b,*l=map(int,sys.stdin.read().rsplit())
l.sort(reverse=True)
print(l[b-1])