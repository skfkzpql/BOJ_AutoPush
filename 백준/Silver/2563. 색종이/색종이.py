a, *b = map(int,open(0).read().rstrip().split())

l = [[0]*100 for i in range(100)]

for i in range(a):
    for j in range(10):
        for k in range(10):
            l[b[2*i]+j][b[2*i+1]+k]=1

count = 0
for i in range(100):
    count += l[i].count(1)

print(count)

