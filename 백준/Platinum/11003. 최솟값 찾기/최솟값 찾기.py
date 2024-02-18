from collections import deque

n,l,*a = map(int,open(0).read().split())

dq =deque()

for i in range(n):
    while dq and dq[-1][0] > a[i]:
        dq.pop()
    dq.append((a[i],i))
    if dq[0][1] <= i - l:
        dq.popleft()
    print(dq[0][0], end = ' ')