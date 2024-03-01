f = open(0)
n = int(f.readline())
l = [tuple(map(int, line.rsplit())) for line in f.readlines()]

l.sort(key= lambda x: (x[1], x[0]))

cnt = 0
last_end = 0
for i in l:
    if last_end <= i[0]:
        last_end = i[1]
        cnt += 1

print(cnt)