from bisect import *

f=open(0)
s = f.readline().rstrip()
q = int(f.readline())

keys = [chr(ord('a')+i) for i in range(26)]

d = dict(zip(keys, [[] for _ in range(26)]))

for i in range(len(s)):
    c = s[i]
    d[c].append(i)

for i in range(q):
    a, b, c = f.readline().rsplit()
    start = bisect_left(d[a], int(b))
    end = bisect_right(d[a], int(c))
    print(end-start)