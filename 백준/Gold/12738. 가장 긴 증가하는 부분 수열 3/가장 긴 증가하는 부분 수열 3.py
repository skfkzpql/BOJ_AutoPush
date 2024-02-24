import bisect

N = int(input())
A = list(map(int,input().split()))

bst = [1e9] * N

maxIdx = 0

for i in range(N):
    a = A[i]
    idx = bisect.bisect_left(bst, a)
    bst[idx] = a
    maxIdx = max(maxIdx, idx + 1)


print(maxIdx)