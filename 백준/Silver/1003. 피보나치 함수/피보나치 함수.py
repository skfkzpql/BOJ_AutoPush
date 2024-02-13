import sys
t = int(sys.stdin.readline())

n = list(map(int,sys.stdin.read().rsplit()))
m = max(n)

l = [[0,0] for _ in range(m + 1)]

l[0] = [1,0]
if m > 0:
    l[1] = [0,1]

if m > 1:
    for i in range(2, m + 1):
        l[i][0] = l[i-1][0] + l[i-2][0]
        l[i][1] = l[i-1][1] + l[i-2][1]

for i in n:
    print(*l[i])
