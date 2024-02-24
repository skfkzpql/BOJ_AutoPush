import bisect

N = int(input())
A = list(map(int,input().split()))

bst = [1e6] * N

maxIdx = 0

for i in range(N):
    a = A[i]

    idx = bisect.bisect_left(bst, a)
    bst[idx] = a
    maxIdx = max(maxIdx, idx)

print(maxIdx + 1)