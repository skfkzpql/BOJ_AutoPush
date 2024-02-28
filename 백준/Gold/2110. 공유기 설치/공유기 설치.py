import sys

N, C, *l = map(int, sys.stdin.read().rsplit())
l.sort()

start, end = 1, l[-1] - l[0]
max_length = 0

while start <= end:
    mid = (start + end) // 2

    count = 1
    last = l[0]
    for i in l:
        if i - last >= mid:
            count += 1
            last = i

    if count >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)
