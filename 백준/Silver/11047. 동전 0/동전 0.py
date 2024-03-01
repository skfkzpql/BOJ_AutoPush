n, k, *a = map(int, open(0).read().rsplit())

cnt = 0
for i in range(n - 1, -1, -1):
    if k >= a[i]:
        cnt += k // a[i]
        k %= a[i]
    if k == 0:
        break
        
print(cnt)
