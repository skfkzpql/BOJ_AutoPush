n, *l = map(int, open(0).read().rsplit())

print(sum([(i+1)*j for i, j in enumerate(sorted(l, reverse=True))]))