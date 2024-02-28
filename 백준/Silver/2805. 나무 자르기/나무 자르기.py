import sys

N, M, *l = map(int, sys.stdin.read().rsplit())

start, end = 1, max(l)


while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in l:
        count += i-mid if i>mid else 0
    
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
