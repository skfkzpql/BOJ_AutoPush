n, m, *l = map(int, open(0).read().rsplit())

part_sum = sum(l[:m])
max_v = part_sum
for i in range(n-m):
    part_sum = part_sum- l[i] + l[i+m]
    max_v = max(max_v, part_sum)

print(max_v)