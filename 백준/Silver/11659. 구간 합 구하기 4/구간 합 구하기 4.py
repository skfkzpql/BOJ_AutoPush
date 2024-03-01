import sys

n, m = map(int, sys.stdin.readline().rsplit())
l = list(map(int, sys.stdin.readline().rsplit()))

a = [0] * (n + 2)
z = [0] * (n + 2)
total = sum(l)

for i in range(n):
    a[i + 1] = a[i] + l[i]
    z[n-i] = z[n-i+1] + l[n-i-1]

for _ in range(m):
    x, y = map(int,sys.stdin.readline().rsplit())
    print(total - a[x - 1] - z[y + 1])