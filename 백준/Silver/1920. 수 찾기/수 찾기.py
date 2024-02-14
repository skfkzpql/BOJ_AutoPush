import sys

n, a, m, b = sys.stdin.readlines()

a = a.rsplit()
b = b.rsplit()

s = set(a).intersection(set(b))

for i in b:
    if i in s:
        print(1)
    else:
        print(0)