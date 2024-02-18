from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque(eval(sys.stdin.readline().rstrip()))
    
    l, r = 0, 0
    rev = False
    e = True
    for k in p:
        if k == 'R':
            rev = ~rev
        elif len(arr) == 0:
            e = False
            break
        else:
            if rev:
                arr.pop()
            else:
                arr.popleft()
    
    if e:
        if rev:
            arr.reverse()
        print("[", end="")
        print(*arr,sep=",",end="")
        print("]")
    else:
        print("error")
