import sys

l = []

k=int(sys.stdin.readline().rstrip())

for i in range(k):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        l.pop()
    else:
        l.append(a)

print(sum(l))