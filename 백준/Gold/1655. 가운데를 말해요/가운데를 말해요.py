import heapq as hq

# 입력 받기
n, *nums = map(int, open(0).read().rsplit())

left_max_heap = []
right_min_heap = []
toggle = True

for num in nums:
    hq.heappush(left_max_heap, -num) if toggle else hq.heappush(right_min_heap, num)
    toggle = not toggle

    if right_min_heap and right_min_heap[0] < -left_max_heap[0]:
        hq.heappush(left_max_heap, -hq.heappop(right_min_heap))
        hq.heappush(right_min_heap, -hq.heappop(left_max_heap))

    print(-left_max_heap[0])