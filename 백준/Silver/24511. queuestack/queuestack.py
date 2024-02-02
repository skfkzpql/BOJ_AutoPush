import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
a = deque(map(int,sys.stdin.readline().rsplit()))
b = deque(map(int,sys.stdin.readline().rsplit()))
c = int(sys.stdin.readline().rstrip())
d = deque(map(int,sys.stdin.readline().rsplit()))

queue = deque()
for i in range(n):
    if a[i] != 1:
        queue.append(b[i])

for i in range(c):
    queue.appendleft(d[i])
    print(queue.pop(), end=' ')
