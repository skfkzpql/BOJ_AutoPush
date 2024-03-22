import heapq as hq

n, *l = map(int, open(0).read().rsplit())
hl = []
hr = []

for i in l:
    if len(hl) == len(hr):
        hq.heappush(hl, -i)
    else:
        hq.heappush(hr, i)

    if hr and hr[0] < -hl[0]:
        a = hq.heappop(hl)
        b = hq.heappop(hr)
        hq.heappush(hl, -b)
        hq.heappush(hr, -a)

    print(-hl[0])
