import heapq

f = list(map(int,open(0).read().rsplit()[1:]))

l=[]

for i in f:
    if i == 0:
        if len(l) == 0:
            print(0)
        else:
            print(heapq.heappop(l)[1])
    else:
        heapq.heappush(l, (abs(i), i))