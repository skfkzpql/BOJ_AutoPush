import bisect

N = int(input())
A = list(map(int, input().split()))

bst = []
idx = []
answer = []

max_length = 0

for A_i in A:
    cur_idx = bisect.bisect_left(bst, A_i)

    if max_length == cur_idx:
        bst.append(A_i)
        max_length += 1
    else:
        bst[cur_idx] = A_i
    idx.append(cur_idx)

print(max_length)
max_length -= 1

for i in range(N-1,-1,-1):
    if idx[i] == max_length:
        answer.insert(0,A[i])
        max_length -= 1
        if max_length == -1:
            break
    
print(*answer)
