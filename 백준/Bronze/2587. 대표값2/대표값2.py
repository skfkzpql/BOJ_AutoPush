import sys

l=list(map(int,sys.stdin.read().rsplit()))
l.sort()
print(int(sum(l)/5),l[2],sep='\n')