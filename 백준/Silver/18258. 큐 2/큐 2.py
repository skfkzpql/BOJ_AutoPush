import sys
from collections import deque

n = int(sys.stdin.readline())
l = list(sys.stdin.readline().rstrip() for i in range(n))
d=deque()
for i in range(0,n):
    try:
        a = l[i]
        if a.startswith('push'):
            a,b=a.split()
            d.appendleft(b)
        elif a == 'pop':
            print(d.pop())
        elif a == 'size':
            print(len(d))
        elif a == 'empty':
            print('01'[+(not d)])
        elif a == 'front':
            print(d[-1])
        elif a =='back':
            print(d[0])
    except:
        print(-1)