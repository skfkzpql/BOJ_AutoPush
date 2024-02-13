n = list(map(int,open(0).read().rsplit()))[1:]

l = [1] * 11

l[0] = 1
l[1] = 1
l[2] = 2


for i in range(3,len(l)):
    l[i] = sum(l[i-3:i])

for i in n:
    print(l[i])