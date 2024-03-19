k, n, m = map(int, open(0).read().rsplit())
a = k*n-m
if a < 0:
    a = 0
print(a)