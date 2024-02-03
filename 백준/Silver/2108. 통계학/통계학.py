from collections import deque
import math
n, *l = map(int,open(0).read().split())
l = deque(sorted(l))

print(round(sum(l)/len(l)))
print(l[n//2])

s=set(l)
count = 0
s=dict(zip(s,[0 for i in range(len(s))]))

for i in l:
    s[i] += 1

c = deque()
for i, j in s.items():
    if j > count:
        c.clear()
        c.append(i)
        count = j
    elif j == count:
        c.append(i)


print(sorted(list(c))[len(c)>1])
    
print(l[-1]-l[0])