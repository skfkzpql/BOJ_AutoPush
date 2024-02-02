import sys
from collections import deque

n, *a = map(str,sys.stdin.read().splitlines())
d=deque()
for i in range(int(n)):
    try:
        b = a[i]
        if a[i].startswith('1'):
            d.appendleft(b.split()[1])
        elif a[i].startswith('2'):
            d.append(b.split()[1])
        elif a[i].startswith('3'):
            print(d.popleft())
        elif a[i].startswith('4'):
            print(d.pop())
        elif a[i].startswith('5'):
            print(len(d))
        elif a[i].startswith('6'):
            print(+(not d))
        elif a[i].startswith('7'):
            print(d[0])
        elif a[i].startswith('8'):
            print(d[-1])
    except:
        print(-1)