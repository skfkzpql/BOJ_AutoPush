import bisect

N = int(input())
A = list(map(int, input().split()))

bst = [A[0]]
idx = []

max_length = 0

for A_i in A:
    if bst[-1] < A_i:
        bst.append(A_i)
        max_length += 1
        cur_idx = max_length

    else:
        cur_idx = bisect.bisect_left(bst, A_i)
        bst[cur_idx] = A_i

    idx.append(cur_idx)

print(max_length +1)

answer = []

for i in range(N-1,-1,-1):
    if idx[i] == max_length:
        answer.append(A[i])
        max_length -= 1
        if max_length == -1:
            break
    
print(*reversed(answer))