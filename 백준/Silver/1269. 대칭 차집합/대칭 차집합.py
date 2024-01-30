import sys

a,b,*l=map(int,sys.stdin.read().rsplit())

c={*l[:a]}
d={*l[a:]}

print(len(c.symmetric_difference(d)))
